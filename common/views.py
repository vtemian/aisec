from django.shortcuts import  render
from dashboard import views as dashboard

def base(request):
    if request.user.is_authenticated():
      return dashboard.open(request)
    else:
      return render(request, 'login.html')
