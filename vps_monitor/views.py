from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from forms import *

from remote import *

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            login(request,user)
            next_url = request.GET.get('next','/')
            return HttpResponseRedirect(next_url)
    else:
        form = LoginForm()
    return render_to_response('login.html',context_instance=RequestContext(request,{"form":form}))

def logout_view(request):
    logout(request)
    return login_view(request)

@login_required(login_url='/login/')
def index(request):
    stat = viewMemory() + '\n' + viewNetwork() + '\n' + viewDisk()
    print stat
    stat = stat.replace(" ", "&nbsp;&nbsp;").replace("\n", "<br/>")
    return HttpResponse(stat)
