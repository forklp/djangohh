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
