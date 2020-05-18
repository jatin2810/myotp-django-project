from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from accounts.models import User
from .serializers import (
    PhoneTokenCreateSerializer, PhoneTokenValidateSerializer
)
# from .utils import user_detail
from accounts.authy_api import send_verfication_code,verify_sent_code
from django.shortcuts import get_object_or_404


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)




class GenerateOTP(CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = PhoneTokenCreateSerializer
    # print(queryset)
    def post(self, request, format=None):
        # Get the patient if present or result None.
        # user=User.objects.filter(phone_number=request.data['phone_number'])
        user = get_object_or_404(User, pk=request.data['phone_number'])
        # userd=User.get_model_fields(user)
        print(request.data['phone_number'])
        # ser = self.serializer_class(
        #     data=request.data,
        #     context={'request': request}
        # )
        # if ser.is_valid():
            # token = PhoneToken.create_otp_for_number(
            #     request.data.get('phone_number')
            # )
        print(user)
        try:
            token = send_verfication_code(user)
            data = json.loads(token.text)
            print(data['success'])
            if data['success'] == False:
                return Response({
                'reason' : "Verication codevnjdsbvodbsobvnodsb sent."
                })

            else:
                return Response({
                'message' : 'verification code sent successfully'
                })
        except Exception as e:
            # messages.add_message(self.request, messages.ERROR,
            #                     'verification code not sent. \n'
            #                     'Please re-register.')
            return Response({
            'reason' : "Verication code not sent."
            })



            # if token:
            #     phone_token = self.serializer_class(
            #         token, context={'request': request}
            #     )
            #     data = phone_token.data
            #     if getattr(settings, 'PHONE_LOGIN_DEBUG', False):
            #         data['debug'] = token.otp
            #     return Response(data)
            # return Response({
            #     'reason': "you can not have more than {n} attempts per day, please try again tomorrow".format(
            #         n=getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 10))}, status=status.HTTP_403_FORBIDDEN)
        # return Response(
        #     {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#
#
# class ValidateOTP(CreateAPIView):
#     queryset = PhoneToken.objects.all()
#     serializer_class = PhoneTokenValidateSerializer
# from django.contrib.auth import get_user_model
# from phonenumber_field.formfields import PhoneNumberField
# from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
#
# from accounts.models import User
#
#
# class PhoneTokenCreateSerializer(ModelSerializer):
#     phone_number = serializers.CharField(validators=PhoneNumberField().validators)
#
#     class Meta:
#         model = PhoneToken
#         fields = ('pk', 'phone_number')
#
#
# class PhoneTokenUser(ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def post(self, request, format=None):
#         # Get the patient if present or result None.
#         ser = self.serializer_class(
#             data=request.data, context={'request': request}
#         )
#         if ser.is_valid():
#             pk = request.data.get("pk")
#             otp = request.data.get("otp")
#             try:
#                 user = authenticate(request, pk=pk, otp=otp)
#                 if user:
#                     last_login = user.last_login
#                 login(request, user)
#                 response = user_detail(user, last_login)
#                 return Response(response, status=status.HTTP_200_OK)
#             except ObjectDoesNotExist:
#                 return Response(
#                     {'reason': "OTP doesn't exist"},
#                     status=status.HTTP_406_NOT_ACCEPTABLE
#                 )
#         return Response(
#             {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
