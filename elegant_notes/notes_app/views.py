from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
from .models import Note
from .forms import NoteCreateForm,NoteUpdateForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="/account/login/")
def home_view(request):
    notes = Note.objects.filter(author=request.user.id).order_by('updated_on')
    context = {'notes': notes}
    return render(request, 'home.html', context)


def delete_view(request,pk):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method. Use DELETE.'}, status=400)

    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note not found'}, status=404)

    note.delete()
    return JsonResponse({'message': 'Note deleted successfully'}, status=200)


def create_view(request):
    form=NoteCreateForm()

    if request.method == "POST":
        form=NoteCreateForm(request.POST)

        if form.is_valid():
            note_obj=form.save(commit=False)
            note_obj.author=request.user
            note_obj.save()
            return JsonResponse({'message': 'Note created successfully'}, status=200)
    return JsonResponse({'message': 'Request method not allowed'}, status=405)

def update_view(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note not found'}, status=404)
    form = NoteUpdateForm(instance=note)


    if request.method == "POST":
        form = NoteUpdateForm(request.POST)

    
        if form.is_valid():
            note.title = form.cleaned_data['title']
            note.description = form.cleaned_data['description']
            note.save()
            return JsonResponse({'message': 'Note updated successfully'}, status=200)
    return JsonResponse({'message': 'Request method not allowed'}, status=405)
