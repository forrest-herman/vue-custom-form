from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserRecord(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    business_name = models.CharField(max_length=150)
    year_of_incorp = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    marital_status = models.CharField(max_length=150)
    number_of_children = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    data = models.JSONField(null=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.name