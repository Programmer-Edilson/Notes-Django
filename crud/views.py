from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

# Create your views here.

status = {-1: "To Do",
        0 : "Doing",
        1 : "Done" }

@login_required
def list_notes(request):
    notes = Note.objects.filter(user=request.user)
    for note in notes:
        note.status = status[note.status]
    context = {'notes': notes}
    return render(request, 'list_notes.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Note saved successfully")
            return redirect('notes')
        else:
            messages.warning(request, "Error! Invalid note")
            return redirect('notes')
    form = NoteForm()
    context = {'form': form}
    return render(request, 'create.html', context)

@login_required
def update(request, pk):
    note = Note.objects.get(pk=pk)

    if note is None or request.user != note.user:
        messages.warning(request, "Error, Invalid note")
        return redirect('notes')

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully")
            return redirect('notes')
        else:
            messages.success(request, "Error! Invalid note")
            return redirect('notes')
    
    form = NoteForm(initial={
        'title' : note.title,
        'description': note.description,
        'status': note.status}, instance=note)
    context = {'form': form, 'id' : note.id}
    return render(request, 'update_note.html', context)
    
@login_required
def delete(request, pk):
    note = Note.objects.get(pk=pk)

    if note is None or request.user != note.user:
        messages.warning(request, "Error! Invalid note")
        return redirect('notes')

    note.delete()
    messages.warning(request, "Note deleted successfully")
    return redirect('notes')

@login_required
def profile(request):
    user = request.user
    form = {'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email' : user.email,
            'notes' : Note.objects.filter(user=user).count(),
            'date' : user.date_joined,
    }

    context = {'form': form}
    return render(request, 'profile.html', context)
