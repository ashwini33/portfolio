from django.db import models

# Create your models here.
class Bug(models.Model):
    issue=models.CharField(max_length=512)
    discription=models.TextField()
    visual=models.ImageField(upload_to="bug/images", null=True, blank=True)
    solution=models.TextField(null=True, blank=True)
    reference=models.TextField(null=True, blank=True)
    datetime=models.DateTimeField()
    name=models.CharField(max_length=48,)


#    def __str__(self):
#        if self.name.count()==0:
#            from datetime import datetime
#            now=datetime.now.strftime("%d_%B_%Y_%H:%M:%S")
#            return f"bug_{now}"
#        else:
#            return f"bug_{name}"

