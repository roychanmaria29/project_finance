from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('customer', views.customer, name='customer'),
    path('home',views.home,name='home'),



]