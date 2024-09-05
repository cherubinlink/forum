from django.contrib import admin
from .models import Suject,Group,GroupMenbre,Document,Message

# Register your models here.


class SujectAdmin(admin.ModelAdmin):
    list_display = ['noms_suj']
admin.site.register(Suject, SujectAdmin)


admin.site.register(Group)
admin.site.register(GroupMenbre)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['auteur','suject','noms_doc']
admin.site.register(Document, DocumentAdmin)

admin.site.register(Message)
