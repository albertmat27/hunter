from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django import forms
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    c = {}
    c.update(csrf(request))
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    template = loader.get_template('auth.html')
    context = RequestContext(request,{'state':state, 'username': username})
    return HttpResponse(template.render(context))

    #return render_to_response('auth.html', {'state':state, 'username': username})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("success")
    else:
        form = UserCreationForm()

    template = loader.get_template("registration/register.html")
    context = RequestContext(request, {'form': form,})    
    return HttpResponse(template.render(context))
    #return render(request, "registration/register.html", {'form': form,})