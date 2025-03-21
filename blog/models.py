from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content =  models.TextField()
    date_created = models.DateTimeField(blank=True , null=True)
    updated_At = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
