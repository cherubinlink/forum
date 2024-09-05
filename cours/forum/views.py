from django.shortcuts import render,redirect
from .models import Suject,Document,Group,GroupMenbre,Message
from authuser.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm

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
    group = Group.objects.all().order_by('-date_creer')[0:4]
    
    
    message = Message.objects.filter(
        Q(document__suject__noms_suj__icontains=q)
    ).order_by('-creer_message', '-modifier_message')
    
    context = {
        
        'suject':suject,
        'document':document,
        'document_count':document_count,
        'message':message,
        'group':group
    }
    return render(request,'forum/accueil.html',context)

# zomme activite
def activite(request):
    message = Message.objects.all()
    
    context = {
        'message':message
    }
    return render(request,'forum/activite.html',context)


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

# creer un document
def creer_document(request):
    sujects = Suject.objects.all()
    
    if request.method == 'POST':
        suject_noms = request.POST.get('suject')
        
        # Assurez-vous que le champ 'suject' existe dans le formulaire
        if suject_noms:
            suject,created = Suject.objects.get_or_create(noms_suj=suject_noms)
            
            Document.objects.create(
                auteur = request.user,
                suject = suject,
                noms_doc = request.POST.get('noms_doc'),
                description = request.POST.get('description')
                
            )
            return redirect('accueil')
    else:
        form = DocumentForm()
    context = {
        'form':form,
        'sujects':sujects
    }
    return render(request,'forum/creer_document.html',context)


# mdifier un document
def modifier_document(request,pk):
    document = Document.objects.get(id=pk)
    suject = Suject.objects.all()
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = DocumentForm(instance=document)
    context = {
        'document':document,
        'suject':suject,
        'form':form
    }
    return render(request,'forum/modifier_document.html',context)


# supprimer un document
def delete(request,pk):
    document = Document.objects.get(id=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('accueil')
    context = {
        'obj':document
    }
    return render(request,'forum/delete.html',context)


# supprimer un message
def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    
    if request.method == 'POST':
        message.delete()
        return redirect('accueil')
    
    context = {
        'obj':message
    }
    return render(request,'forum/delete.html',context)



# suject
def suject(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    sujects = Suject.objects.filter(noms_suj__icontains=q)
    
    context = {
        'sujects':sujects
    }
    
    # ajouter le message si aucun suject n'est trouver
    if not sujects:
        context['message'] = "Aucun suject trouver pour votre recherche"
        
    return render(request,'forum/suject.html',context)









