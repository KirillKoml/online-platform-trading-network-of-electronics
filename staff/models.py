from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    """Модель для сотрудников"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.email}'