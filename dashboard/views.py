from django.http import HttpResponse
from emergency_notifications import views

def open(request):
  views.send_email("vladtemian@gmail.com")
  return HttpResponse("test")
