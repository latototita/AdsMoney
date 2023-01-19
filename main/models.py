from django.db import models 
from django.contrib.auth.models import User
import datetime
from cloudinary.models import CloudinaryField
# Create your models here.
class AdsLink(models.Model):
	name =models.CharField(max_length=1000)
	def __str__(self):
		return self.name


class Websitelink(models.Model):
	name =models.CharField(max_length=1000)
	def __str__(self):
		return self.name
class WebAdsContainer(models.Model):
	name =models.TextField(max_length=1000000)
	def __str__(self):
		return self.name


class Wallet(models.Model):
	name =models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Withdraw(models.Model):
	customer =models.ForeignKey(User,
                                on_delete=models.CASCADE)
	amount =models.IntegerField()
	wallet=models.ForeignKey(Wallet,
                                on_delete=models.CASCADE)
	address= models.CharField(max_length=1000,default=0)
	date =models.DateTimeField(default=datetime.datetime.today)
	status =models.BooleanField(default=False)
	def __str__(self):
		return self.name

class Referred(models.Model):
	personwhorefferred = models.CharField(max_length=1000,default=0)
	personrefferred= models.CharField(max_length=1000)
	date_refferred =models.DateTimeField(default=datetime.datetime.today)
	paid=models.BooleanField(default=False)
	def __str__(self):
		return self.personrefferred

	class Meta:
		ordering = ('-date_refferred', )

class ReferralBonu(models.Model):
	person = models.CharField(max_length=1000,default=0)
	amount= models.CharField(max_length=1000,default=0)
	paid= models.BooleanField(default=False)
	date_paid =models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.person

	class Meta:
		ordering = ('-date_paid', )


class Clicks(models.Model):
	name=models.ForeignKey(User,
                                on_delete=models.CASCADE)
	number =models.IntegerField()


