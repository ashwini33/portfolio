from django.db import models

# Create your models here.
class Weblog(models.Model):
    title=models.CharField(max_length=128)
    summary=models.TextField()
    image=models.ImageField(upload_to="weblog/images", null=True, blank=True)
