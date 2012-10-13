from django.shortcuts import  render
from discussion import *

def base(request):
    if request.user.is_authenticated():
        return 
    else:
        return render(request, 'login.html')
