from django.db import models
from django_filters import rest_framework as filters

class User(models.Model):
	username=models.CharField(max_length=20)
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	passwordmodels=models.CharField(max_length=20)

	def __str__(self):
		return self.username

class Part(models.Model):
	name=models.CharField(max_length=20)
	price=models.DecimalField(max_digits=6, decimal_places=2)
	stock=models.DecimalField(max_digits=6, decimal_places=2)
	is_available=models.BooleanField(default=True)
	category=models.CharField(max_length=20)

	def __str__(self):
		return self.name+' '+self.category


class Cart(models.Model):
	user=models.OneToOneField('User', on_delete=models.CASCADE)
	items=models.ManyToManyField('Part', through='CartItem')
	total_price=models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.user+' '+self.total_price

class CartItem(models.Model):
	cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
	part=models.ForeignKey(Part, on_delete=models.CASCADE)
	quantity=models.DecimalField(max_digits=6, decimal_places=2)
	date= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.part+' '+self.quantity


class Order(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	value=models.DecimalField(max_digits=6, decimal_places=2)
	address=models.CharField(max_length=20)
	items=models.ManyToManyField('Part', through='OrderItem')
	status=models.CharField(max_length=20)

	def __str__(self):
		return self.value+' '+self.status

class OrderItem(models.Model):
	order=models.ForeignKey(Order, on_delete=models.CASCADE)
	part=models.ForeignKey(Part, on_delete=models.CASCADE)
	quantity=models.DecimalField(max_digits=6, decimal_places=2)
	date= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.part+' '+self.quantity

