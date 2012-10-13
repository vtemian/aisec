from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

from notification.backends.base import NotificationBackend

class EmailBackend(NotificationBackend):
    """
    Email delivery backend.
    """
    
    title = _("Email")
    slug = 'email'

    def get_addresses(self, recipients):
        addresses = []
        for recipient in recipients:
            addresse = getattr(recipient, 'email', None)
            if addresse:
                addresses.append(addresse)

        return addresses

    def send(self, subject, body, recipients, *args, **kwargs):
        addresses = self.get_addresses(recipients)
        if addresses:
            return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, addresses)

