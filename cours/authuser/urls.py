from django.urls import path
from authuser import views

urlpatterns = [
    # login
    path('login',views.login_view,name='login'),
    
    # register
    path('register',views.register_view,name='register'),
    
    path('logout',views.logout_user,name='logout-user'),
    
    # profile
    path('profile',views.profile,name='profile'),
    
    
    # modifier le profile
    path('modifier_profile',views.modifier_profile,name='modifier-profile')
]
