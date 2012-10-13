from datetime import datetime
import hashlib
import random
from django.http import HttpResponse
from django.shortcuts import  render, render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from django.utils.hashcompat import sha_constructor

from account.models import PasswordReset
from game import views
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# list of mobile User Agents
from mobile.views import start as mobile_start

mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-', 'ipad','android'
	]

mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone', 'Android', 'iPad', 'webOS' ]


def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser

def base(request):
    if mobileBrowser(request):
        if request.user.is_authenticated():
            return mobile_start(request)
        else:
            return render(request, 'm_login.html')
    else:
        if request.user.is_authenticated():
            return views.start(request)
        else:
            return render(request, 'login.html')

def reset_password_instance(request):
    if request.method == 'POST':
        fromEmail = "staff@outclan.com"
        toEmail = request.POST.get('email')
        
        try:
            reset_instance = PasswordReset.objects.get(email=toEmail, done=False)
            return HttpResponse(simplejson.dumps({'message':"There is a request. Please check again!"}))
        except PasswordReset.DoesNotExist:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Outclan - reset password"
            msg['From'] = fromEmail
            msg['To'] = toEmail

            salt = sha_constructor(str(random.random())).hexdigest()[:5]
            token = sha_constructor(salt + toEmail).hexdigest()

            PasswordReset(email=toEmail, token=token).save()

            link = "http://www.outclan.com/password/"+token

            text = "Hi!\n"+link+"\n"
            html = """\
            <html>
              <head></head>
              <body>
                <p>Hi!<br>
                   """+link+"""<br>
                </p>
              </body>
            </html>
            """

            username = 'vtemian'
            password = "seleus00"

            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            msg.attach(part1)
            msg.attach(part2)

            s = smtplib.SMTP('smtp.sendgrid.net', 587)

            s.login(username, password)

            s.sendmail(fromEmail, toEmail, msg.as_string())

            s.quit()
            return HttpResponse(simplejson.dumps({'message':"An email has been sent to you!"}))
    return HttpResponse('Not here!')

def reset_password(request, token):
    reset_instance = PasswordReset.objects.get(token=token)
    now = datetime.datetime.now()
    context = {}
    if now-reset_instance.created_at < datetime.timedelta(minutes=30):
        context['token'] = token
        return render_to_response('change_password.html',
                              context,
                              context_instance=RequestContext(request))
    else:
        reset_instance.done = True
        reset_instance.save()
        context['email'] = reset_instance.email
        return render_to_response('fail_change_password.html',
                              context,
                              context_instance=RequestContext(request))