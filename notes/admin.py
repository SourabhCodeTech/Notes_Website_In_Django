from django.contrib import admin

from notes.models import Note

# Register your models here.
list_display = ['notes']


@admin.register(Note)
class notes(admin.ModelAdmin):
    list_display
