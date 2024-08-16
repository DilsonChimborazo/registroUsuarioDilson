from django.shortcuts import render,redirect
from .models import Persona
from .form import personaform

# Create your views here.

def registrouser(request):
    if request.method == 'POST':
        form = personaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuario')
    else:
        form = personaform()
    return render(request,
    template_name='/registroUsuario.html',context={'form':
    form})
