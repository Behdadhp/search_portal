from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

genders = (
    ("Male", "Herr"),
    ("Female", "Frau"),
    ("Diverse", "Diverse")
    )

titles = (
    ("Dr", "Dr"),
    ("-", "-")
)

specialist_groups = (
    ("Hals-Nasen-Ohrenheilkunde", "Hals-Nasen-Ohrenheilkunde"),
    ("Frauenheilkunde", "Frauenheilkunde"),
    ("Orthopädie", "Orthopädie"),
    ("Dermatologie", "Dermatologie"),
)

class Doctors(models.Model):
    gender             = models.CharField(max_length=8,choices=genders)
    title              = models.CharField(max_length=8,choices=titles)
    first_name         = models.CharField(max_length=32,blank=False,null=False)
    last_name          = models.CharField(max_length=32,blank=False,null=False)
    specialist_group   = models.CharField(max_length=32, choices=specialist_groups)
    mail               = models.EmailField(max_length=64,blank=False,null=False,default="mail@mail.com")

    def __str__(self):
        return (self.first_name + " " + self.last_name)

class Insurances(models.Model):
    insurance = models.CharField(max_length=32,blank=False,null=False)

    def __str__(self):
        return self.insurance

contracts = (
        ("Tinnitus", "Tinnitus"),
        ("Hello Baby","Hello baby"),
        ("Schmerztherapie", "Schmerztherapie"),
        ("Hautkrebsscreening", "Hautkrebsscreening"),
        )
