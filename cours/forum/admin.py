from django.contrib import admin
from .models import Suject,Group,GroupAdmin,Document,Message

# Register your models here.

admin.site.register(Suject)
admin.site.register(Group)
admin.site.register(GroupAdmin)
admin.site.register(Document)
admin.site.register(Message)
