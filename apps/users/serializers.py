from rest_framework import serializers
from .models import CustomUser, UserEncoding


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class PhotoSerializer(serializers.Serializer):
    photo1 = serializers.ImageField()
    photo2 = serializers.ImageField()
    photo3 = serializers.ImageField()

    def create(self, validated_data):
        return UserEncoding.objects.create(**validated_data)




