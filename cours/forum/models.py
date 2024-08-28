from django.db import models
from authuser.models import User

# Create your models here.




class Group(models.Model):
    noms_group = models.CharField(max_length=200)
    description = models.TextField()
    date_creer = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.noms_group
    

class Suject(models.Model):
    noms_suj = models.CharField(max_length=200)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.noms_suj


class GroupAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    

class Document(models.Model):
    auteur = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    suject = models.ForeignKey(Suject,on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    noms_doc = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    participant = models.ManyToManyField(User, related_name='participant',blank=True)
    modifier_doc = models.DateTimeField(auto_now=True)
    creer_doc = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-modifier_doc','-creer_doc']
        
    def __str__(self):
        return self.noms_doc
    
    
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    corp = models.TextField()
    modifier_message = models.DateTimeField(auto_now=True)
    creer_message = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-creer_message']
        
    def __str__(self):
        return self.corp
    

