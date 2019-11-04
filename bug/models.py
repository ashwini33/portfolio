from django.db import models

# Create your models here.
class Bug(models.Model):
    issue=models.CharField(max_length=512)
    discription=models.TextField()
    visual=models.ImageField(upload_to="bug/images", null=True, blank=True)
    solution=models.TextField(null=True, blank=True)
    reference=models.TextField(null=True, blank=True)
    datetime=models.DateTimeField()
    name=models.CharField(max_length=48, null=True, blank=True)


    def __str__(self):
        if self.name:
            return f"bug_{self.name}_{self.datetime}"
        else:
            return f"bug_{self.datetime}"

