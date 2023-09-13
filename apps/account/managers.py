from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from common.constants import SUPER_ADMIN, ADMIN, TEACHER, DIRECTOR


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ Создает и сохраняет пользователя с введенным им email и паролем. """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email.lower())
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_student(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)

    def create_teacher(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', TEACHER)
        return self._create_user(email, password, **extra_fields)

    def create_director(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', DIRECTOR)
        return self._create_user(email, password, **extra_fields)

    def create_admin(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', ADMIN)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_type', SUPER_ADMIN)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, password, **extra_fields)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)