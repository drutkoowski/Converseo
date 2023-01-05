from datetime import datetime, timedelta

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


def get_current_date():
    return datetime.today()


def get_expire_date():
    return datetime.today() + timedelta(minutes=1)


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=105, unique=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, default="default_avatar.png")
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", ]
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def get_avatar_path(self):
        try:
            return self.avatar.path
        except:
            return ""


class Post(models.Model):
    author = models.CharField(max_length=30)


class SearchQueue(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=get_current_date)
    expires_at = models.DateTimeField(default=get_expire_date)
