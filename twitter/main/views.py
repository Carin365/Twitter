# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from main.forms import UserCreationForm
from main.forms import UserCreateForm
from main.forms import RegistrationForm, LoginForm
from main.models import Users, Auth
from main.forms import UsersForm
from main.models import Tweet
from main.forms import TweetForm
from django.contrib.auth.decorators import login_required 


@login_required
def home(request):
    if request.user.is_authenticated():
        return redirect('sesion')
    else:
        return render_to_response('home.html', {
    }, RequestContext(request))

def userss(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sesion')
    return render_to_response('Change.html',{
        'form': form,
    }, RequestContext(request))


def all(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sesion')
    return render_to_response('all.html',{
        'form': form,
    }, RequestContext(request))

def edit_user(request):
    #user = get_object_or_404(Users)
    form = UsersForm()
    if request.method == 'POST':
     form = UsersForm(request.POST)
     if form.is_valid():
        form.save()
     return redirect('/sesion/')
    return render_to_response('sesion.html',{
        'form': form,
    }, RequestContext(request))




def add_User(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_User.html', {
        'form': form,
    }, RequestContext(request))


def User_Registration(request):

    if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                    user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
                    user.save()
#                    users = user.get.profile()
#                    users.name = form.cleaned_data['name']
#                    users.birthday = form.cleaned_data['birthday']
#                    users.save()
                    users = Users(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
                    users.save()
                    return HttpResponseRedirect('/')
            else:
                    return render_to_response('RegisterUser.html', {'form': form}, context_instance=RequestContext(request))
    else:
            ''' user is not submitting the form, show them a blank registration form '''
            form = RegistrationForm()
            context = {'form': form}
            return render_to_response('RegisterUser.html', context, context_instance=RequestContext(request))


def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        users = authenticate(username=username, password=password)
                        if users is not None:
                                login(request, users)
                                return redirect('sesion')
                        else:
                                return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('home.html', context, context_instance=RequestContext(request))


def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/')


def sesion(request):

    tweet = Tweet.objects.all()
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sesion')
    return render_to_response('sesion.html', {
       'form': form,'tweet': tweet,
    }, RequestContext(request))

def profile(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sesion')
    return render_to_response('Change.html',{
        'form': form,
    }, RequestContext(request))

     #return render_to_response('profile.html',{

    #}, RequestContext(request))
