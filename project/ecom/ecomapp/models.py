from django.db import models


# Create your models here.
class Signup(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    mobno = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=200, blank=True)
    password = models.CharField(max_length=50, default='')
    c_password = models.CharField(max_length=50, default='')
    profile_image = models.FileField(blank=False)

    class Meta:
        db_table = "ecomp"