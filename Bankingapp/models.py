from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 45)
	phone = models.CharField(max_length=15, primary_key = True,default="")
	Current_balance = models.IntegerField(blank = False)

	def __str__(self):
		return self.username+" | "+str(self.Current_balance)