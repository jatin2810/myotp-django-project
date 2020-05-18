from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import logout
from .views import ( RegisterView, DashboardView,
                    LoginView, PhoneVerificationView,
                    IndexView,view1)
from django.contrib.auth import views as auth_views

app_name='accounts'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_page'),
    url(r'^register/$', RegisterView.as_view(), name="register_url"),
    url(r'^login/', view1, name="login_url"),
    url(r'^verify/$', PhoneVerificationView, name="phone_verification_url"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard_url"),
    url(r'^xyz/$', LoginView,name="LoginView"),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),

]
