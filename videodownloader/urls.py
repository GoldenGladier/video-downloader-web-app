"""videodownloader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
# from videodownloader import views

from downloader import urls as downloader_app_urls
# from django.urls import re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('downloadByItag', views.download_By_Itag, name="downloadByItag"),
    path('', include(downloader_app_urls)),
    path('celery-progress/', include('celery_progress.urls')),
]
