import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fakeusers.settings')

import django
django.setup()

import random
from userapp.models import User
from faker import Faker

fakegen = Faker()
def populate(N):

    for entry in range(N):

        fake_name= fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_mail = fakegen.email()

        user_pop = User.objects.get_or_create(firstname=fake_name, lastname=fake_lastname, email=fake_mail)[0]



if __name__=='__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')