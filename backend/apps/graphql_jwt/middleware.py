# NOTE TODO: need to port over entire graphql-jwt lib to local,
# remove current third_party refresh token app and replace with local

import warnings
import json
from datetime import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

from graphene_django.settings import graphene_settings
from graphql import GraphQLError

from .exceptions import JSONWebTokenError
from .path import PathDict
from .settings import jwt_settings
from .refresh_token.shortcuts import get_refresh_token, refresh_token_lazy
from .utils import get_http_authorization, get_http_refresh_authorization, get_token_argument, get_payload

__all__ = [
    'allow_any',
    'JSONWebTokenMiddleware',
]


def allow_any(info, **kwargs):
    field = getattr(
        info.schema,
        'get_{}_type'.format(info.operation.operation),
    )().fields.get(info.field_name)

    if field is None:
        return False

    graphene_type = getattr(field.type, 'graphene_type', None)

    return graphene_type is not None and\
        issubclass(graphene_type, tuple(jwt_settings.JWT_ALLOW_ANY_CLASSES))


def _authenticate(request):
    is_anonymous = not hasattr(request, 'user') or request.user.is_anonymous
    # print('anon:', is_anonymous)
    return is_anonymous and get_http_authorization(request) is not None


class DjangoMiddleware():

    def __init__(self, get_response=None):
        # super(DjangoMiddleware, self).__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):
        if '/admin/' in request.path:
            return self.get_response(request)
        else:
            body = None
            if request.body:
                body = json.loads(request.body.decode('utf-8'))

            # if request is None or getattr(request, '_jwt_token_auth', False):
            #     user = None

            # NOTE: all authenticate yo anon's should be replaced with redirects to login
            response = self.get_response(request)
            print(response.status_code)
            request_token = get_http_authorization(request)
            try:
                get_payload(request_token, request)
            except JSONWebTokenError as err:
                refresh = get_http_refresh_authorization(request)
                if refresh:
                    try:
                        refresh_token = get_refresh_token(refresh, request)
                        if refresh_token.is_expired(request):
                            # raise exceptions.JSONWebTokenError(_('Refresh token is expired'))
                            return JsonResponse({
                                'errors': [{'message': 'authenticate yo un-tokened anon ass!'}],
                            }, status=401)

                        expires = datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
                        
                        refresh_expires = refresh_token.created +\
                            jwt_settings.JWT_REFRESH_EXPIRATION_DELTA

                        payload = jwt_settings.JWT_PAYLOAD_HANDLER(refresh_token.user, request)
                        token = jwt_settings.JWT_ENCODE_HANDLER(payload, request)

                        refresh_token.rotate(request)
                        refreshed_token = refresh_token_lazy(refresh_token.user)
                        # NOTE: send x-username or similar so frontend gets username (from payload)
                        response.set_cookie(
                            jwt_settings.JWT_COOKIE_NAME,
                            token,
                            expires=expires,
                            httponly=True,
                            secure=jwt_settings.JWT_COOKIE_SECURE
                        )
                        response.set_cookie(
                            jwt_settings.JWT_REFRESH_TOKEN_COOKIE_NAME,
                            refreshed_token,
                            expires=refresh_expires,
                            httponly=True,
                            secure=jwt_settings.JWT_COOKIE_SECURE
                        )
                        # operation = list(json.loads(response.content.decode('utf-8'))["data"])[0]
                        # NOTE: in frontend, if result.tokensRefreshed, call the this.submit() query again
                        response.content = '{"errors": [ {"message": "tokensRefreshed"}]}'.encode('utf-8')
                        # response.status_code = 401
                        # raise GraphQLError('tokensRefreshed')
                    except JSONWebTokenError as err:
                        return JsonResponse({
                            'errors': [{'message': 'authenticate yo un-tokened anon ass!'}],
                        }, status=401)
                    
                elif (body and 'mutation' in body.get('query') and 'login' in body.get('query')) or settings.DEBUG:
                    pass
                else:
                    return JsonResponse({
                        'errors': [{'message': 'authenticate yo un-tokened anon ass!'}],
                    }, status=401)

            patch_vary_headers(response, ('Authorization',))
            # if expired:
            #     response['x-token'] = 'memes'
            #     response['x-refresh-token'] = 'refresh memes'
        
            return response


class JSONWebTokenMiddleware:

    def __init__(self):
        self.cached_allow_any = set()

        if jwt_settings.JWT_ALLOW_ARGUMENT:
            self.cached_authentication = PathDict()

    def authenticate_context(self, info, **kwargs):
        root_path = info.path[0]

        if root_path not in self.cached_allow_any:
            if jwt_settings.JWT_ALLOW_ANY_HANDLER(info, **kwargs):
                self.cached_allow_any.add(root_path)
            else:
                return True
        return False

    def resolve(self, next, root, info, **kwargs):
        
        context = info.context
        token_argument = get_token_argument(context, **kwargs)

        # if jwt_settings.JWT_ALLOW_ARGUMENT and token_argument is None:
        #     user = self.cached_authentication.parent(info.path)

        #     if user is not None:
        #         context.user = user

        #     elif hasattr(context, 'user'):
        #         if hasattr(context, 'session'):
        #             context.user = get_user(context)
        #         else:
        #             context.user = AnonymousUser()

        # print('MEMMEMEMEEMMS', _authenticate(context), self.authenticate_context(info, **kwargs))
        if ((_authenticate(context) or token_argument is not None) and
                self.authenticate_context(info, **kwargs)):
            # print('MEMMEMEMEEMMS2222')
            # try:
            user = authenticate(request=context, **kwargs)
            # print(user)
            # except JSONWebTokenError as err:
            #     return None
            if user is not None:
                context.user = user

                if jwt_settings.JWT_ALLOW_ARGUMENT:
                    self.cached_authentication.insert(info.path, user)

        return next(root, info, **kwargs)