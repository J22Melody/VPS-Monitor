from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils import simplejson as json

from forms import *
from models import *
from remote import *

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
            next_url = request.GET.get('next','/')
            return HttpResponseRedirect(next_url)
    else:
        form = LoginForm()
    return render_to_response('login.html',context_instance=RequestContext(request,{'form':form}))

def logout_view(request):
    logout(request)
    return login_view(request)

@login_required(login_url='/login/')
def index(request):
    remote_list = Remote.objects.all()
    return render_to_response('index.html',context_instance=RequestContext(request,{'remote_list': remote_list}))

def get_os(request):
    options = fromRequest(request)
    data = SSH.getInstance(**options).execCommand('cat /etc/issue')
    return HttpResponse(json.dumps({'success':True, 'data': data}),mimetype="application/json")

def get_mem(request):
    options = fromRequest(request)
    data = SSH.getInstance(**options).execCommand('free -m').split('\n')[2]
    return HttpResponse(json.dumps({'success':True, 'data': data}),mimetype="application/json")

def fromRequest(request):
    return {
        'hostname': request.GET.get('hostname'),
        'port': int(request.GET.get('port')),
        'username': request.GET.get('username'),
        'password': request.GET.get('password')
    }
