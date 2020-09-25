from django.db import models

# Create your models here.

class Students(models.Model):
    sid = models.CharField(max_length=150)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.fname

class Meta:
    db_table = "students"

