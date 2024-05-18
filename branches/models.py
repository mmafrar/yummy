from django.db import models


# Create your models here.
class Day(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day_of_week = models.CharField(
        max_length=9, choices=DAY_CHOICES, unique=True)

    def __str__(self):
        return self.day_of_week


class Branch(models.Model):
    branch_name = models.CharField(max_length=150)
    branch_address = models.CharField(max_length=200)
    branch_contact = models.CharField(max_length=150)
    branch_image = models.ImageField(
        upload_to='branches', null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    day = models.ManyToManyField(
        Day, related_name='branches', blank=True)

    def is_closed(self):
        return self.opening_time is None and self.closing_time is None

    def __str__(self):
        return self.branch_name
