from django.urls import path
from .views import *
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view,name='register'),
    path('activate/',activate,name='activate'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate')
    
]
