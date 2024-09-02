from django.urls import path
from forum import views

urlpatterns = [
    # accueil
    path('',views.accueil,name='accueil'),
    
    # activite
    path('activite',views.activite,name='activite'),
    
    # creer document 
    path('creer_document',views.creer_document,name='creer-document'),
    
    # supprimer un document
    path('delete/<int:pk>/',views.delete,name='delete'),
    
    # document
    path('document/<int:pk>/',views.document,name='document'),
    
    # modifier document
    path('modifier_document/<int:pk>/',views.modifier_document,name='modifier-document'),
    
    # supprimer un message
    path('delete_message/<int:pk>/',views.delete_message,name='delete-message'),
    
    # suject
    path('suject',views.suject,name='suject'),
    
    
    # group
    path('group',views.group,name='group'),
    
    # creer un group
    path('creer_group',views.creer_group,name='creer-group'),
    
    
    
]