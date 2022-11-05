from django.shortcuts import render

from .models import Note


def index(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'webapp/index.html', context)


def note(request, id=1):
    note = Note.objects.get(pk=id)
    context = {
        'note': note
    }
    return render(request, 'webapp/note.html', context)