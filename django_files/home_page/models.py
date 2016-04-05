from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db.models.signals import post_save

# class SignUp(models.Model):
# 	username = models.CharField(max_length=20)
# 	password = models.CharField(max_length=20)
# 	email = models.EmailField()
# 	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
# 	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

# 	def __unicode__(self):
# 		return self.username

# 	def __str__(self):
# 		return self.username

class MyManager(UserManager):
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        super().create_superuser(username, first_name, last_name, email, password, **extra_fileds)
        #or do something to save your model by yourself;
    # def create_user(self, username, first_name,)
    def create_user(self, username, email=None, password=None):
    	super().create_user(username, email, password)


class UserProfile(AbstractUser):
	user_mobile = models.IntegerField(null=True)
	stars = models.IntegerField(default=0)


	REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

class Games(models.Model):
	tutorial = models.BooleanField(default = False)
	game1 = models.BooleanField(default = False)
	users = models.OneToOneField(UserProfile)


