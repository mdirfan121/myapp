from django.db import models

# Create your models here.

class info(models.Model):
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	message=models.CharField(max_length=200)

	def __str__(self):
		return self.firstname