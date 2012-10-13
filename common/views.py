from django.shortcuts import  render
from django.views.generic.simple import direct_to_template

def base(request):
    if request.user.is_authenticated():
        return direct_to_template(request, 'index.html')
    else:
        return render(request, 'login.html')