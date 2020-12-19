from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('passgen/',views.passgen,name="passgen"),
    path('logout/',views.logout,name="logout"),
    path('generate/',views.generate,name="generate"),
    path('notgenerate/',views.notgenerate,name="notgenerate"),
    path('<str:query>/', views.home,name="home"),
]