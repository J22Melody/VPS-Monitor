from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import json

from forms import *
from models import *
from remote import monitors


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            next_url = request.GET.get('next', '/')
            return HttpResponseRedirect(next_url)
    else:
        form = LoginForm()
    return render_to_response('login.html', context_instance=RequestContext(request, {'form': form}))


def logout_view(request):
    logout(request)
    return login_view(request)


@login_required(login_url='/login/')
def index(request):
    remotes = Remote.objects.all()
    return render_to_response('index.html', context_instance=RequestContext(request, {'remote_list': remotes}))


def get_info(request):
    monitor = monitors[request.GET.get('id')]
    method = request.GET.get('method')
    data = getattr(monitor, method)()
    return HttpResponse(json.dumps({'success': True, 'data': data}), mimetype="application/json")
