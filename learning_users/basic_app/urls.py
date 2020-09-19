from django.urls import path
from .import views

#TEMPLATE URL
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('special', views.special, name='special'),
    path('user_login', views.user_login, name='user_login'),

]