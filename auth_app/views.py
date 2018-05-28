from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request, emailToPlayer):
    subject = 'w'
    message = 'w'
    res = send_mail(subject , message , "mahan@gmail.com", [emailToPlayer],fail_silently=False,)
    return HttpResponse('s')