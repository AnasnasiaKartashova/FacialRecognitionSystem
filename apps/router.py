from django.urls import path, include

routes = [
    path("user/", include("apps.users.urls")),
]
