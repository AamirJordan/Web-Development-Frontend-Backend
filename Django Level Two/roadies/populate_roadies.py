import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","roadies.settings")


import django
django.setup()

import random
from roadieapp.models import Roadies
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for entry in range(N):

        fake_name = fakegen.name().split()
        fake_first_name = fakegen.name()[0]
        fake_last_name = fakegen.name()[1]


        errggggg = Roadies.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name)


if __name__ == '__main__':
    print("populating script")
    populate(25)
    print("populating process completed")
