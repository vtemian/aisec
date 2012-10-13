import hashlib
from django.http import HttpResponse
from django.contrib.auth.models import User, check_password
from django.contrib.auth import authenticate, login as auth_login
from django.utils import simplejson
from account.form import UserRegister, UserLogin, ResetPassword
from django.views.decorators.csrf import csrf_exempt

from account.models import UserProfile, PasswordReset

def register(request):
    if request.method == "POST":
        form =  UserRegister(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            user.save()
            gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(request.POST.get('email')).hexdigest()
            userprofile = UserProfile(user=user, gravatar_url=gravatar_url).save()
            
            auth_login(request,authenticate(username=request.POST['username'], password=request.POST['password']))
            return HttpResponse(simplejson.dumps({'ok': '/'}))
        else:
            return HttpResponse(simplejson.dumps(form.errors))

def login(request):
    form = UserLogin(request.POST)
    if form.is_valid():
        user = form.get_auth_user()
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponse(simplejson.dumps({'ok': '/'}))
            return HttpResponse(simplejson.dumps({'disabled': 'This account has been disabled'}))
        return HttpResponse(simplejson.dumps({'not': 'Incorect username or password'}))
    else:
        return HttpResponse(simplejson.dumps(form.errors))