from django.db import models

# Create your models here.

class Transaction(models.Model):
	date = models.DateTimeField("Date")
	source = models.CharField("From", max_length=64 , default="", blank=True)
	hashCode = models.CharField("Hash", max_length=64 , default="", blank=True)
	destination = models.CharField("To", max_length=64 , default="", blank=True)
	blockHash = models.CharField("BlockHash", max_length=64 , default="", blank=True)
	blockNumber = models.IntegerField("BlockNumber", default=0)
	montant = models.FloatField("Value", default=0)
	
	
	def __str__(self):
		return self.hashCode

class Block(models.Model):
	blockNumber = models.IntegerField("BlockNumber", default=0)
	blockHash = models.CharField("BlockHash", max_length=64 , default="", blank=True)
	date = models.DateTimeField("Date")
	reward = models.IntegerField("BlockNumber", default=0)
	miner = models.CharField("Hash", max_length=64 , default="", blank=True)
	
	def __str__(self):
		return self.hashCode
	
class Alias(models.Model):
	alias = models.CharField("Alias", max_length=64 , default="", blank=True)
	adresse = models.CharField("Adresse", max_length=64 , default="", blank=True)
	
	
	def __str__(self):
		return self.hashCode	
	
	
	
