from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import CustomUser, UserEncoding, LateComer
from .serializers import UserSerializers, PhotoSerializer, LateComerSerializer
from rest_framework.response import Response
from apps.functions.train_model import train_model_by_img


class CustomUserApiView(APIView):
    serializer_class = UserSerializers

    def get(self, request):
        serializer = self.serializer_class(CustomUser.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EncodingApiView(APIView):
    serializer_class = PhotoSerializer

    def get(self, request, pk):
        serializer = self.serializer_class(UserEncoding.objects.all(), many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, pk):
        instance = get_object_or_404(CustomUser.objects.all(), id=pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(instance=instance)

        return Response(status=status.HTTP_200_OK)


class LateComerAPIView(APIView):
    def get(self, request):
        serializer = LateComerSerializer(LateComer.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LateComerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
