import datetime

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from django.conf import settings

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from common.constants import STUDENT, TEACHER, ADMIN, DIRECTOR, SUPER_ADMIN
from common.upload_to_file import user_avatar
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Пользователь """
    USER_TYPE = (
        (STUDENT, _('Студент')),
        (TEACHER, _('Преподаватель')),
        (ADMIN, _('Администратор')),
        (DIRECTOR, _('Директор')),
        (SUPER_ADMIN, _('Супер администратор')),
    )
    last_name = models.CharField(_('Фамилия'), max_length=40, blank=True)
    first_name = models.CharField(_('Имя'), max_length=40, blank=True)
    sur_name = models.CharField(_('Отчество'), max_length=50, blank=True, null=True)
    slug = models.SlugField(_("slug"))
    email = models.EmailField(_('email'), unique=True)
    avatar = ProcessedImageField(verbose_name=_('Обложка'), upload_to=user_avatar,
                                 format='webp', processors=[ResizeToFill(500, 500)],
                                 options={'quality': 90}, null=True, blank=True)
    user_type = models.CharField(_("Пользователь является:"), max_length=40,
                                 choices=USER_TYPE, default=STUDENT)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'sur_name']

    class Meta:
        db_table = 'User'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return str(self.get_full_name())

    def get_full_name(self):
        """ Возвращает first_name, last_name и part_name с пробелом между ними. """
        if self.sur_name:
            return f"{self.first_name} {self.last_name} {self.sur_name}".strip()
        return f"{self.first_name} {self.last_name}".strip()

    def get_user_type(self):
        return dict(self.USER_TYPE)[self.user_type]

    def last_seen(self):
        return cache.get(f'seen_{self.email}')

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False
