from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.title

class Product(models.Model):
	title = models.CharField(max_length=255, null=True)
	image=models.ImageField(upload_to='media/', null=True, blank=True,
	width_field="width_field", height_field="height_field")
	
	height_field = models.IntegerField(default=100)
	width_field = models.IntegerField(default=100)
	
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	price = models.CharField(max_length=30, null=True)
	brand = models.CharField(max_length=255, null=True)
	productcode = models.CharField(max_length=10, primary_key=True)
	rewardpoint = models.CharField(max_length=30, null=True)
	availability = models.CharField(max_length=30, null=True)
	description = models.TextField(blank=True, null=True)
    
	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse("main:detail", kwargs={"productcode": self.productcode})

class Cart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField()
	total = models.IntegerField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.product.title
