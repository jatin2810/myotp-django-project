from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import User

User = get_user_model()


class PhoneTokenCreateSerializer(ModelSerializer):
    phone_number = serializers.CharField(validators=PhoneNumberField().validators)

    class Meta:
        model = User
        fields = ('pk', 'phone_number')


class PhoneTokenUser(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PhoneTokenValidateSerializer(ModelSerializer):
    pk = serializers.IntegerField()
    otp = serializers.CharField(max_length=40)

    class Meta:
        model = User
        fields = ('pk', 'otp')
