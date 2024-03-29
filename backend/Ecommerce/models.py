from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    added_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ('-added_at',)

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.name

    class Meta():
        ordering = ('-ordered_at',)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta():
        ordering = ('user',)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total = models.FloatField()

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['items__name']

