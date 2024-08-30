from django.shortcuts import render,redirect
from .models import Suject,Document,Group,GroupAdmin,Message
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


# accueil
def accueil(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    suject = Suject.objects.all().order_by('-id')[0:5]
    document = Document.objects.filter(
        Q(suject__noms_suj__icontains=q) |
        Q(noms_doc__icontains=q)
    )
    
    document_count = document.count()
    
    message = Message.objects.filter(
        Q(document__suject__noms_suj__icontains=q)
    ).order_by('-creer_message', '-modifier_message')
    
    context = {
        'suject':suject,
        'document':document,
        'document_count':document_count,
        'message':message
    }
    return render(request,'forum/accueil.html',context)

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
def document(request, pk):
    document = Document.objects.get(id=pk)
    message = document.message_set.all().order_by('-creer_message')
    participant = document.participant.all()
    
    if request.method == 'POST':
        creer_message = Message.objects.create(
            user = request.user,
            document = document,
            corp = request.POST.get('corps')
        )
        document.participant.add(request.user)
        return redirect('document', pk=document.id)
    context = {
        'document':document,
        'message':message,
        'participant':participant
    }
    return render(request,'forum/document.html',context)

# mdifier un document
def modifier_document(request):
    return render(request,'forum/modifier_document.html')

# suject
def suject(request):
    return render(request,'forum/suject.html')

