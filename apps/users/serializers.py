from rest_framework import serializers
from .models import CustomUser, Encoding


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class EncodingSerializer(serializers.Serializer):
    user_encoding = serializers.CharField()





