"""trial URL Configuration
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
from django.urls import path
from .views import SearchVideo, create_video, delete_video, detail_video, update_video, delete_video, VideoCategoryList


urlpatterns = [
    path('create/', create_video.as_view(), name='video-create'),
    path('<int:pk>/', detail_video.as_view(), name='video-detail'),
    path('<int:pk>/update', update_video.as_view(), name='video-update'),
    path('<int:pk>/delete', delete_video.as_view(), name='video-delete'),
    path('category/<int:pk>', VideoCategoryList.as_view(), name='category-list'),
    path('search/', SearchVideo.as_view(), name='video-search'),
]