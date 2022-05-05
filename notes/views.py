from django.shortcuts import render
from .models import Note
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        if title and desc:
            notes = Note(noteTitle=title, noteDesc=desc)
            notes.save()
            if notes:
                messages.success(request, "Your Note Add!")
    return render(request, 'index.html')


def notes(request):
    showNotes = Note.objects.all()
    return render(request, 'notes.html', {'showNotes': showNotes})
