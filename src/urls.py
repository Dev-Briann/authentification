from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django_email_verification import urls as mail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('accounts/',include('accounts.urls')),
     path('email/', include(mail_urls)),
   
]
if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)