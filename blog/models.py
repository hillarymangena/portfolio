from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    detail = models.TextField()

