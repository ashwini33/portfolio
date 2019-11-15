from django.db import models
from django.http import HttpResponse
import datetime

# Create your models here.
class Bug(models.Model):
    issue=models.CharField(max_length=256)
    status=models.BooleanField(default=False)
    summary=models.CharField(max_length=512, null=True, blank=True,)
    description=models.TextField()
    visual=models.ImageField(upload_to="bug/images", null=True, blank=True)
    solution=models.TextField(null=True, blank=True)
    reference=models.TextField(null=True, blank=True)
    datetime=models.DateTimeField(auto_now_add=True,)


    def __str__(self):
        if self.issue:
            return f"bug_{self.issue}_{self.datetime}"
        else:
            return f"bug_{self.datetime}"

    def bug_status(self):
        if self.status:
            return f"Solved"
        else:
            return f"Not Solved"
