import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","final_project.settings")


import django
django.setup()

import random
from fin_app.models import Enduser
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):


        fake_name = fakegen.name().split()
        fake_first_name = fakegen.name()[0]
        fake_last_name = fakegen.name()[1]
        fake_email = fakegen.email()

        datafake = Enduser.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)


if __name__ == '__main__':
    print("populating in process")
    populate(28)
    print("populating completed")
