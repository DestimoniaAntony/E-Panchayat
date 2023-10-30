"""
URL configuration for e_panchayath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from e_panchayath_app import admin_urls, staff_urls, users_urls

from e_panchayath_app.views import IndexView,User_RegView,loginview,Staff_RegView

urlpatterns = [
    # path('admin', admin.site.urls),
    path('',IndexView.as_view()),
    path('path',IndexView.as_view()),
    path('login',loginview.as_view()),
    path('userreg',User_RegView.as_view()),
    path('staffreg',Staff_RegView.as_view()),
    path('users/',users_urls.urls()),
    path('staff/',staff_urls.urls()),
    path('admin/',admin_urls.urls()),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)