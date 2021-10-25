from django.contrib import admin
from . models import Chore, UserChore


class ChoreAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Chore, ChoreAdmin)
admin.site.register(UserChore)