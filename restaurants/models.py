from django.db import models

# Create your models here.

class Day(models.Model):
    day_of_week = models.CharField(max_length=150)

    def __str__(self):
        return self.day_of_week

class Branch(models.Model):
    branch_name = models.CharField(max_length=150)
    branch_address = models.CharField(max_length=200)
    branch_contact = models.CharField(max_length=150)
    branch_image = models.ImageField(upload_to='file_uploads/', null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def is_closed(self):
        return self.opening_time is None and self.closing_time is None

    def __str__(self):
        return self.branch_name
