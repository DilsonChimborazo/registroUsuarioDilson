from django.shortcuts import render,redirect
from .models import Persona
from .form import form

# Create your views here.

def registrouser(request):
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuario')
    else:
        form = form()
    return render(request,'/registroUsuario.html',{'form':form})
