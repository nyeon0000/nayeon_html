"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #mainpage URL 연결하기 with 별명사용
    path('',views.main, name="showmain"),

    # firstpage URL 연결하기 with 별명사용
    path('fisrtpage/', views.showfirst, name="onemain"),

    # secondpage URL 연결하기 with 별명사용
    path('secondpage/', views.showsecond, name="twomain"),
    path('<str:id>',views.detail, name="detail"),
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),
    path('',include('main.urls')),
    # auth를 이용한 로그인 구현
    # path('accounts/',include('accounts.urls')),
    # allauth를 이용한 구현
    path('accounts/',include('allauth.urls')),
    path('users/',include('users.urls')),
    
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



