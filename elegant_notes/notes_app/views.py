from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import Note
from .forms import NoteCreateForm,NoteUpdateForm



def home_view(request):
    user = request.user
    notes = Note.objects.filter(author=user).order_by('updated_on')
    context = {'notes': notes}
    return render(request, 'home.html', context)
