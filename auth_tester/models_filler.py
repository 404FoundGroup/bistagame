import auth_tester.setup_django
from auth_app import models
users = ('armor','sed','mahan','mamad','sajjad')
for user in users:
    models.User.objects.get_or_create(username=user,email=user+'@gmail.com',password='password')