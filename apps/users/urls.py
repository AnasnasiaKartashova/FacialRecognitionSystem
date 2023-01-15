from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
    path("users-list/", CustomUserApiView.as_view()),
    path("encoding/", EncodingApiView.as_view())
]