from django.shortcuts import render
from .models import Mod, Perevod

def modsmanager_home(request):
    mod = Mod.objects.all()
    return render(request, 'modsmanager/mods.html', {'mods': mod})

def modtranslations(request):
    perevod = Perevod.objects.all()
    return render(request, 'modsmanager/modtranslations.html', {'tsblevota': perevod})