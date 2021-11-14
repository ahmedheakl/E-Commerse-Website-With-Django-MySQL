from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import related
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)
    def __str__(self):
        return f'{self.category}'

class Listing(models.Model):
    title = models.CharField(max_length=60)
    dateofcreation = models.DateTimeField(default=timezone.now)
    description = models.CharField(null=True, max_length=300)
    startbid = models.IntegerField()
    image_link = models.CharField(max_length=200, default=None, blank=True, null=True)
    currentbid= models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='similar_listings')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_creator_listings')
    watchers = models.ManyToManyField(User, blank=True, related_name='watched_lisitings')
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return f'{self.title} - {self.startbid}'

class Bid(models.Model):
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.FloatField()
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    createdDate = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_comments')
    

