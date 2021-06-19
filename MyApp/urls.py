from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('webDev/', views.webDev, name="webDev"),
    path('appDev/', views.appDev, name="appDev"),
    path('webScrapping/', views.webScrapping, name="webScrapping"),
    path('mySkill/', views.mySkill, name="mySkill"),
]