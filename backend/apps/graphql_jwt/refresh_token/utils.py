from django.apps import apps
from django.db import transaction
# from .models import RefreshToken

from ..settings import jwt_settings


def get_refresh_token_model():
    return apps.get_model(jwt_settings.JWT_REFRESH_TOKEN_MODEL)


def get_refresh_token_by_model(refresh_token_model, token, context=None):
    return refresh_token_model.objects.get(token=token, revoked__isnull=True)

def revoke_by_user(user, context):
    tokens = user.refresh_tokens.all()
    # NOTE: CHANGE TO bulk_update when updating to django 2.2.5 or greater
    # print(dir(tokens))
    with transaction.atomic():
        for t in tokens:
            t.revoke(context)
