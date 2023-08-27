
from django.db import models

# Create your models here.

class Form(models.Model):
    image=models.FileField(upload_to="image/", max_length=250,null=True,default=None)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    exp=models.CharField(max_length=200)
    cv=models.FileField(upload_to="cv/", max_length=250,null=True,default=None )
    file=models.FileField(upload_to="file/", max_length=250,null=True,default=None)

    def __str__(self):
        return self.name
