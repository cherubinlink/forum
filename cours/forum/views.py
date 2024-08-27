from django.shortcuts import render

# Create your views here.


# accueil
def accueil(request):
    return render(request,'forum/accueil.html')

# zomme activite
def activite(request):
    return render(request,'forum/activite.html')


# creer un document
def creer_document(request):
    return render(request,'forum/creer_document.html')


# supprimer un document
def delete(request):
    return render(request,'forum/delete.html')

# document
def document(request):
    return render(request,'forum/document.html')

# mdifier un document
def modifier_document(request):
    return render(request,'forum/modifier_document.html')

# suject
def suject(request):
    return render(request,'forum/suject.html')

