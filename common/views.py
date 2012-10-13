from django.shortcuts import  render

def base(request):
    if request.user.is_authenticated():
        return "oky"
    else:
        return render(request, 'login.html')