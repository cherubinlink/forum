from django.urls import path
from authuser import views

urlpatterns = [
    # login
    path('login',views.login,name='login'),
    
    # register
    path('register',views.register,name='register'),
    
    # profile
    path('profile',views.profile,name='profile'),
    
    
    # modifier le profile
    path('modifier_profile',views.modifier_profile,name='modifier-profile')
]
