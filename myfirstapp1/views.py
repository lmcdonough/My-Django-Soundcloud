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

def broadcasts(request):
    context = {'games': 'this is the games page.'}

    return render(request, 'broadcasts.html', context)


def selected_broadcast(request):
    context = {'selected_game': 'this is the selected game.'}

    return render(request, 'selected_broadcast.html', context)

def sports(request):
    context = {'sports': 'this is the sports page.'}
    
    return render(request, 'sports.html', context)
    
def about(request):
    context = {'about': 'this is the about page.'}
    
    return render(request, 'about.html', context)

def contact(request):
    context = {'contact': 'this is the contact page.'}
    
    return render(request, 'contact.html', context)

def teams(request):
    context = {'teams': 'this is the teams page.'}
    
    return render(request, 'teams.html', context)

def selected_team(request):
    context = {'selected_team': 'this is the selected team page.'}
    
    return render(request, 'selected_team.html', context)
