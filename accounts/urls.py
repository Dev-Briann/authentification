from django.urls import path
from .views import *
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view,name='register'),
    # path('activate/<uidb64>/<token>/',activate,name='activate'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    
    
]
