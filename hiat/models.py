from django.db import models
from decimal import Decimal
from django.core.validators import RegexValidator


"""
Model class for the job. Contains:
    :title: the title of the job;
    :description: the description of the job;
    :date_time: the starting date and time of the job;
    :wage: the wage paid, for doing the job;
    :category: the category of the job;
"""
class Job(models.Model):
    title = models.TextField(default="")
    description = models.TextField(default="")
    date_time = models.DateTimeField()
    wage = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    category = models.TextField(default="")


"""
Model class for the user. Contains:
    :first_name: The first name of the user
    :last_name: The last name of the user
    :skills: The set of skills
    :phone_number: The mobile number of the user
"""
class User(models.Model):
    first_name = models.TextField(default="")
    last_name = models.TextField(default="")
    skills = models.TextField(default="")
    age = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)