from django.shortcuts import  render
from discussion import views

def base(request):
    if request.user.is_authenticated():
        return views.disccusions(request)
    else:
        return render(request, 'login.html')
