from django.db import models

# Create your models here.

class Outpassform(models.Model):
    studentname = models.CharField(max_length=64)
    sklmid = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    studentph = models.CharField(max_length=10)
    parentname = models.CharField(max_length=64)
    parentph = models.CharField(max_length=10)
    year = models.CharField(max_length=64)
    rclass = models.CharField(max_length=64)
    outdate = models.DateField()
    reportingdate = models.DateField()
    reason = models.CharField(max_length=64)
    address = models.CharField(max_length=254)
    proofletter = models.FileField(upload_to="proofphotos/%Y/%m/%d")

    def __str__(self):
        return f"{self.studentname} wants leave for {self.reason}"

class Outpassformaccepted(models.Model):
    studentname = models.CharField(max_length=64)
    sklmid = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    studentph = models.CharField(max_length=10)
    parentname = models.CharField(max_length=64)
    parentph = models.CharField(max_length=10)
    year = models.CharField(max_length=64)
    rclass = models.CharField(max_length=64)
    outdate = models.DateField()
    reportingdate = models.DateField()
    reason = models.CharField(max_length=64)
    address = models.CharField(max_length=254)
    proofletter = models.FileField(upload_to="acceptproofphotos/%Y/%m/%d")

    def __str__(self):
        return f"{self.studentname} wants leave for {self.reason}"