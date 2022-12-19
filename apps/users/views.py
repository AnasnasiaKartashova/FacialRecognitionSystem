from rest_framework import status
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CustomUserApiView(APIView):
    serializer_class = UserSerializers

    def get(self, request):
        serializer = self.serializer_class(CustomUser.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






