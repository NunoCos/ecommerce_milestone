from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.conf import settings
from django_countries.fields import CountryField
import os
# Create your models here.
CATEGORY_CHOICES = (
    ("Women", "Women"),
    ("Men", "Men"),
    ("Kids", "Kids"),
    ("Accessories", "Accessories"),
    ("Cosmetics", "Cosmetics"),
)

ADMIN_CHOICES = (
    ("admin","admin"),
)

SIZE_CHOICES = (
    ("S","S"),
    ("M","M"),
    ("L","L"),
    ("XL","XL"),
)