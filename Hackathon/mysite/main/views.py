from django.shortcuts import render
from django.http import HttpResponse
from .forms import URLForm
import colorsys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .goodvibes import find_HSV
import logging

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            # Perform any desired actions with the form data
            # ...
            (H, S, V) = find_HSV(str(form.cleaned_data["name"]))
            (R, G, B) = colorsys.hsv_to_rgb(H/360, S, V)
            R = int(R * 255)
            G = int(G * 255)
            B = int(B * 255)
            return render(request, "main/home.html", {'R':R, 'G':G, 'B':B})
    else:
        form = URLForm()
    return render(request, 'main/base.html', {'form': form})
    # return render(request, "main/base.html")

def home(request):
    return render(request, "main/home.html", {})
