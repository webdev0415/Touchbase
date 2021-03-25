from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from apps.graphql_jwt.decorators import jwt_cookie



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    
    path('graphql', jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG)))),
    
]
