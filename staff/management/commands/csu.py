
from django.core.management import BaseCommand

from staff.models import Employee

# Импортирую данные для почты админа и пароль
from dotenv import load_dotenv
import os
load_dotenv()


class Command(BaseCommand):
    """Команда для создания админа."""
    def handle(self, *args, **options):
        user = Employee.objects.create(email=os.getenv('email'))
        user.set_password(os.getenv('POSTGRES_PASSWORD'))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
