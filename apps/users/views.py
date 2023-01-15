from rest_framework import status
from rest_framework.views import APIView
from .models import CustomUser, Encoding
from .serializers import UserSerializers, EncodingSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CustomUserApiView(APIView):
    serializer_class = UserSerializers

    def get(self, request):
        serializer = self.serializer_class(CustomUser.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EncodingApiView(APIView):
    def get(self, request):
        lst_encode = Encoding.objects.all()
        return Response({'user_encoding': EncodingSerializer(lst_encode, many=True).data})

    def post(self, request):
        serializer = EncodingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_user_encoding = Encoding.objects.create(user_encoding=request.data['user_encoding'])
        return Response({'user_encoding': EncodingSerializer(new_user_encoding).data})



