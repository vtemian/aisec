from django.http import HttpResponse

def open(request):
  return HttpResponse("test")
