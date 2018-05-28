from django.conf.urls import url
from . import views


app_name = 'auth_app'

mail = r'verify/(?P<emailToPlayer>[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+(\.[A-Za-z]{2,4}))/$'

urlpatterns = [
    url(mail ,views.send_email , name = 'sendEmail'),
]