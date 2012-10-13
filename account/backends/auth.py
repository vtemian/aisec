# And finally, here is auth.py
#
import hashlib
from django.contrib.auth.models import User
from openid.consumer.consumer import SUCCESS
from django.core.mail import mail_admins
from account.models import UserProfile

class GoogleBackend:

  def authenticate(self, openid_response):
    if openid_response is None:
      return None
    if openid_response.status != SUCCESS:
      return None

    google_email = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.email')
    google_firstname = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.firstname')
    google_lastname = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.lastname')
    username = google_email.split('@')[0]
    print username
    try:
      user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password='*', email=google_email)
        user.first_name = google_firstname
        user.last_name = google_lastname
        user.save()
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(google_email).hexdigest()
        userprofile = UserProfile(user=user, gravatar_url=gravatar_url).save()
        return user

    return user

  def get_user(self, user_id):

    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None