import hashlib
from django.http import HttpResponse
from django.contrib.auth.models import User, check_password
from django.contrib.auth import authenticate, login as auth_login
from django.utils import simplejson
from django.views.generic.simple import direct_to_template
from account.form import UserRegister, UserLogin, ResetPassword
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect, render
from django.template.context import RequestContext
from account.models import UserProfile

def register(request):
    if request.method == "POST":
        form =  UserRegister(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
                user.save()

                gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(request.POST.get('email')).hexdigest()

                userprofile = UserProfile.objects.create(user = user)
                auth_login(request,authenticate(username=request.POST['username'], password=request.POST['password']))
                return HttpResponse(simplejson.dumps({'ok': '/'}))
            except Exception as exp:
                return HttpResponse(exp.message)
        else:
            return HttpResponse(simplejson.dumps(form.errors))


def login(request):
    if request.method == 'POST':
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
    else:
        return direct_to_template(request, 'login.html')

def change_password(request):
    if request.method == 'POST':
        form = ResetPassword(request.POST)
        if form.is_valid():
            try:
                token = request.POST.get('token')
                password = request.POST.get('newpassword')
                passwordReset =  PasswordReset.objects.get(token=token)
                email = passwordReset.email
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                passwordReset.done = True
                passwordReset.save()
                return HttpResponse(simplejson.dumps({'message':'The password had been change!'}))
            except Exception:
                return HttpResponse(simplejson.dumps({'error':'Something went wrong...'}))
        else:
            return HttpResponse(simplejson.dumps(form.errors))
    return HttpResponse('Junky!')

def user_menu(request):
    render_context = {}
    user = UserStats.objects.get(user = UserProfile.objects.get(user=request.user))
    render_context['userprofile'] = user

    division_user = UserDivision.objects.get(user=user)
    render_context['division'] = division_user

    return render_context

def profile(request, profile_id):
    context = user_menu(request)
    userpro= UserProfile.objects.get(pk=profile_id)
    context['userpro'] = userpro
    stats=UserStats.objects.get(user=userpro.user_id)
    context['stats'] = stats
    userdiv=UserDivision.objects.get(user=userpro.user_id)
    context['userdiv'] = userdiv
    medals=UserMedals.objects.filter(user=stats)
    context['medals'] = medals
    medalsnr=0
    for medal in medals:
        medalsnr=medalsnr+1
    context['medalsnr']= medalsnr

    return render_to_response('profile.html',
        context,
        context_instance=RequestContext(request))


def help(request):
    context = user_menu(request)
    return render_to_response('help.html', context, context_instance=RequestContext(request))
