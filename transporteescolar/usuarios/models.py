from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups_set',
        blank=True,
        help_text='Los grupos a los que este usuario pertenece.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permission_set',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos del usuario',
    )
