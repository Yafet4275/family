from django.contrib import admin
#from Django.onlineShop.gestionPedidos.views import search
from . models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ChoreResource(resources.ModelResource):
    class Meta:
        model=Chore


class ChoreAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['name', 'state', 'state']
    list_display=('id', 'name', 'start_task', 'imagen', 'state', 'created', 'updated')
    #readonly_fields=('created', 'updated')
    resource_class=ChoreResource


class UserChoreResource(resources.ModelResource):
    class Meta:
        model=UserChore


class UserChoreAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['name', 'lastname', 'gener']
    list_display=('id', 'name', 'lastName', 'gener')
    #readonly_fields=('created', 'updated')
    resource_class=UserChoreResource


admin.site.register(Chore, ChoreAdmin)
admin.site.register(UserChore, UserChoreAdmin)