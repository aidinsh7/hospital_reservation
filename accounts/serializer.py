from rest_framework import serializers
from .models import OtpModel, UserModel


def validate(data):
    if UserModel.objects.filter(username=data.get('username')).exists():
        raise serializers.ValidationError({'username': 'this user name is exists'})
    if UserModel.objects.filter(phone_number=data.get('phone_number')).exists():
        raise serializers.ValidationError({'phone_number': 'this phone number is exists'})
    return data


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class OtpSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtpModel
        fields = '__all__'
