from django.db import models
from django.utils import timezone
# Create your models here.
class Port(models.Model):

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_time',)

    def __unicode__(self):
        return self.title

class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    size = models.CharField(max_length=1, choices=SIZES)
    name = models.TextField(null=True)
    price = models.CharField(max_length=5,null=True)

    def __unicode__(self):
        return self.size

