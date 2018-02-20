from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator

# Create your models here.


def get_upload_path(instance, filename):
    return 'question3/{}/%Y/%m/%d/{}'.format(type(instance), filename)


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    ACCESS_LEVELS = (
        (1,'SuperAdmin'),
        (2,'Admin'),
        (3,'User'),
    )

    objects = AccountManager()
    # primary email
    email = models.EmailField('email', unique=True, blank=False, null=False)
    full_name = models.CharField('full_name', blank=True, null=True, max_length=400)
    phone = models.CharField(max_length=8,unique=True,blank=True,null=True)
    is_staff = models.BooleanField('staff status', default=False)

    is_active = models.BooleanField('active', default=False) # account is allowed
    is_verified = models.BooleanField('active', default=False) # account email is valid

    access_level = models.IntegerField(choices=ACCESS_LEVELS, default=3)

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def __unicode__(self):
        return self.email

    def is_super_admin(self):
        return self.access_level == 1

    def is_admin(self):
        return self.access_level == 2

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


@receiver(post_save, sender=Account)
def update_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_verified:
        subject = 'Activate Your Feedback Account'
        message = render_to_string('authentication/account_activation_email.html', {
            'user': instance,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(instance.pk)).decode('utf-8'),
            'token': default_token_generator.make_token(instance),
        })

        instance.email_user(subject, message, from_email='no-reply@mail.feedback.com')
