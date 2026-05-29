import os
import sys
import django
import datetime
from UserService import UserService

sys.path.append("C:\Users\Sandeep\PycharmProjects\Django-Project\sos")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sos.settings')
django.setup()

def testadd():
    params = {
        'firstname': 'shyam',
        'lastname': 'sharma',
        'loginid': '980shyam',
        'password': 'abc',
        'dob': datetime.date(2020, 1, 1),
        'address': 'indore'
    }
    service = UserService
    service.add(params)

testadd()