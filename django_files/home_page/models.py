from django.db import models

class SignUp(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.username

	def __str__(self):
		return self.username

	# Create your models here.
