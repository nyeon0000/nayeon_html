
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #mainpage URL 연결하기 with 별명사용
    path('', include('main.urls')),
    path('accounts/',include('allauth.urls')),
    path('users/',include('users.urls')),
    
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
