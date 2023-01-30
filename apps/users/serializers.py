import os
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from .models import CustomUser, UserEncoding, LateComer
from ..functions.train_model import train_model_by_img


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class PhotoSerializer(serializers.Serializer):
    photo1 = serializers.ImageField()
    photo2 = serializers.ImageField()
    photo3 = serializers.ImageField()

    def create(self, validated_data):
        instance = validated_data.pop('instance')
        result = UserEncoding.objects.create(**validated_data)
        encodings = train_model_by_img()
        result.user_encoding1 = encodings[0]
        result.user_encoding2 = encodings[1]
        result.user_encoding3 = encodings[2]
        result.save()
        instance.face_encoding = result
        instance.save()
        for f in os.listdir('media'):
            os.remove(os.path.join('media', f))
        return result




class LateComerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LateComer
        fields = '__all__'
