from django.db import models

# Create your models here.
class UserInput(models.Model):
	encode = models.TextField()
	get_frequency = models.TextField()
	get_key = models.IntegerField(default=0)

	def __str__(self):
		return self.encode