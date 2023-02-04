from django.db import models

# Create your models here.
class PixelList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Color(models.Model):
    color = models.ForeignKey(PixelList, on_delete=models.CASCADE)
    text =models.CharField(max_length=300)

    def __str__(self):
        return self.text
    
class URL(models.Model):
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.url
           
