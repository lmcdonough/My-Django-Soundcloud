import sys
from django.shortcuts import render_to_response, render, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template import Context, Template, RequestContext
from django.template import resolve_variable
import uuid
from django.contrib.auth import authenticate
from django.http import HttpResponse


def home(request):

    context = {'hello': 'hello world'}
    return render(request, 'index.html', context)

def custom_404(request):

    context = {'error_message': 'this is not the page you are looking for...'}
    return render(request, '404.html', context)

def games(request):
    context = {'games': 'this is the games page.'}

    return render(request, 'games.html', context)


def selected_game(request):
    context = {'selected_game': 'this is the selected game.'}

    return render(request, 'selected_game.html', context)


    
