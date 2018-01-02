from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

def get_upload_path(instance, filename):
    return 'hadhari/{}/%Y/%m/%d/{}'.format(type(instance),filename)


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

    objects = AccountManager()
    # primary email
    email = models.EmailField('email', unique=True, blank=False, null=False)
    full_name = models.CharField('full_name', blank=True, null=True, max_length=400)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)

    SUPER_ADMIN = 1
    ADMIN = 2
    MANAGEMENT = 3
    VOLUNTEER = 4
    CLIENTS = 5


    ACCESS_LEVELS = (
        (SUPER_ADMIN, 'Hadhari Super Admin'),
        (ADMIN, 'Admin'),
        (VOLUNTEER, 'Volunteer'),
        (CLIENTS, 'Clients'),
        (MANAGEMENT, 'Management'),
    )

    account_type = models.IntegerField(default=-1, choices=ACCESS_LEVELS)
    account_profile = models.IntegerField(null=True)

    # is_verified = models.BooleanField('verified', default=False)
    # verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def __unicode__(self):
        return self.email


class Branch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    zone = models.CharField(max_length=50,blank=True,null=True)


class Volunteer(models.Model):
    MALE = 0
    FEMALE = 1

    GENDER_CHOICES = (
        (MALE,'Male'),
        (FEMALE,'Female')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dob = models.DateField()

    Branch = models.ForeignKey(Branch)
    picture = models.ImageField(upload_to='boxgirls/%Y/%m/%d/')

    gender = models.IntegerField(choices=GENDER_CHOICES)
    next_of_kin = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    residence = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
