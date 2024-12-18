from django.db import models
from .upload_images_github import GitHubStorage


# Create your models here.
class BigMenu(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='bigmenu/', max_length=600, storage=GitHubStorage())

    def __str__(self):
        return self.title


class SmallMenu(models.Model):
    bigmenu = models.ForeignKey(BigMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='smallmenu/', max_length=600, storage=GitHubStorage())

    def __str__(self):
        return self.title


class Product(models.Model):
    smallmenu = models.ForeignKey(SmallMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/', max_length=600, storage=GitHubStorage())

    def __str__(self):
        return self.title
