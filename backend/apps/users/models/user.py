from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import settings
from apps.common.models import HistoricalModel
from apps.users.managers import UserManager


class User(HistoricalModel, PermissionsMixin, AbstractBaseUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
    )
    first_name = models.CharField(
        _('first name'),
        max_length=settings.MAX_LENGTH_FIRST_NAME,
        validators=[MinLengthValidator(settings.MIN_LENGTH_FIRST_NAME, message=_('First name is too short'))],
        help_text=_(f'Required. {settings.MAX_LENGTH_FIRST_NAME} characters or fewer.'),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=settings.MAX_LENGTH_LAST_NAME,
        validators=[MinLengthValidator(settings.MIN_LENGTH_LAST_NAME, message=_('Last name is too short'))],
        help_text=_(f'Required. {settings.MAX_LENGTH_LAST_NAME} characters or fewer.'),
        blank=True,
        null=True,
    )
    email = models.EmailField(_('email address'), unique=True)
    is_email_verified = models.BooleanField(
        _('email confirm'),
        default=False,
        help_text=_('Indicates whether the user has verified their email address.'),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
