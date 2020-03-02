"""bishe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bisheapp  import views
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('bisheindex', views.index, name='bisheindex'),
    path('event_manage/',views.event_manage),
    path('login_action/', views.login_action),
    path('register/', views.register),
    path('rootevent_manage/',views.rootevent_manage),
    path('rootlogin_action/', views.rootlogin_action),
    path('edit_article/', views.edit_article),
    path('edit_article2/', views.edit_article2),
    path('edit_article3/', views.edit_article3),
    path('gengxingonggao2/', views.gengxingonggao2),
    path('qingchugonggao2/', views.qingchugonggao2),
    path('publish/', views.publish),
    path('rootlogin', views.rootlogin, name='rootlogin'),
    path('backindex', views.backindex, name='backindex'),
    path('rootindex', views.rootindex, name='rootindex'),
    path('successfullogin', views.successfullogin, name='successfullogin'),
    path('yonghuyemian', views.yonghuyemian, name='yonghuyemian'),
    path('yonghuyemian2', views.yonghuyemian2, name='yonghuyemian2'),
    path('yonghuyemian3', views.yonghuyemian3, name='yonghuyemian3'),
    path('wodetiezi', views.wodetiezi, name='wodetiezi'),
    path('map-google', views.map_google, name='map-google'),
    path('fatieyemian', views.fatieyemian, name='fatieyemian'),
    path('gonggao', views.gonggao, name='gonggao'),
    path('gengxingonggao', views.gengxingonggao, name='gengxingonggao'),
    path('qingchugonggao', views.qingchugonggao, name='qingchugonggao'),
    path('cuowuyemian', views.cuowuyemian, name='cuowuyemian'),

]
