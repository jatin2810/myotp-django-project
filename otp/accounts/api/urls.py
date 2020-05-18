from django.urls import path
from accounts.api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('generate/',views.GenerateOTP.as_view(), name="generate"),
    # path('validate/', ValidateOTP.as_view(), name="validate"),
]

# phone number ->otp jayega->otp verify->token return (Login)

# phone_number/full name/country_code/ ->otp bhejega->otp verify -> databases me save karna
