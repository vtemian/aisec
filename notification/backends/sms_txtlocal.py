from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured

from notification.backends.base import NotificationBackend

try:
    from txtlocal.utils import sendSMS
except ImportError:
    raise ImproperlyConfigured('notifications.backends.txtlocal requires incuna-txtlocal. Try pip install incuna-txtlocal.')

class SMSBackend(NotificationBackend):
    """
    SMS delivery backend.
    """
    
    title = _("SMS")
    slug = 'sms'

    def get_numbers(self, recipients):
        numbers = []
        for recipient in recipients:
            cleaned_mobile = getattr(recipient, 'cleaned_mobile', None)
            if cleaned_mobile:
                numbers.append(cleaned_mobile)

        return numbers

    def send(self, subject, body, recipients, *args, **kwargs):
        if hasattr(settings, 'SMS_GATEWAY_USERNAME') and hasattr(settings, 'SMS_GATEWAY_PASSWORD'):
            numbers = self.get_numbers(recipients)

            if numbers:
                sender = getattr(settings, 'SMS_SENDER', None)
                if settings.DEBUG:
                    print "SMS To:%s Sender:%s Body:%s" % (numbers, sender, body)
                if getattr(settings, 'SEND_SMS', False):
                    return sendSMS(numbers, body, settings.SMS_GATEWAY_USERNAME, settings.SMS_GATEWAY_PASSWORD, sender=sender)
                else:
                    print "In order to send SMS notifications add SEND_SMS = True in settings"
        else:
            raise ImproperlyConfigured('SMS_GATEWAY_USERNAME and SMS_GATEWAY_PASSWORD are missing in settings')


