from django.contrib import admin

from .models import Ponytodo

class PonytodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Ponytodo, PonytodoAdmin)
