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
    path('delete',views.delete,name='delete'),
    
    # document
    path('document',views.document,name='document'),
    
    # modifier document
    path('modifier_document',views.modifier_document,name='modifier-document'),
    
    # suject
    path('suject',views.suject,name='suject'),
    
]