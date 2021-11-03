from django.contrib import admin
from . models import Chore, UserChore


class ChoreAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class UserChoreAdmin(admin.ModelAdmin):
    readonly_fields=('lastName', 'gener')


admin.site.register(Chore, ChoreAdmin)
admin.site.register(UserChore, UserChoreAdmin)