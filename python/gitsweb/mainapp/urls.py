from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home),
    path('login', views.login),
    path('log/', views.log),
    path('signup/', views.signup),
    path('test/', views.test),
    path('save', views.save)
]
