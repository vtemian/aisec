from django.http import HttpResponse
from tags.models import Tag

def exists(request, tag_name):
  try:
    Tag.objects.get(name=tag_name)
    return HttpResponse("True")
  except Exception:
    return HttpResponse("False")
