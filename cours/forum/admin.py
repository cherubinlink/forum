from django.contrib import admin
from .models import Suject,Group,GroupMenbre,Document,Message

# Register your models here.

admin.site.register(Suject)
admin.site.register(Group)
admin.site.register(GroupMenbre)
admin.site.register(Document)
admin.site.register(Message)
