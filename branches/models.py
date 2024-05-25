import os
from django.db import models


class Branch(models.Model):
    branch_name = models.CharField(max_length=150)
    branch_address = models.CharField(max_length=200)
    branch_contact = models.CharField(max_length=150)
    branch_image = models.ImageField(
        upload_to='branches', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name

    def delete(self, *args, **kwargs):
        # If there's an associated image, delete it
        if self.branch_image and os.path.isfile(self.branch_image.path):
            os.remove(self.branch_image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # If updating an instance, delete the old image
        if self.pk:
            try:
                old_instance = Branch.objects.get(pk=self.pk)
                if old_instance.branch_image and old_instance.branch_image != self.branch_image:
                    if os.path.isfile(old_instance.branch_image.path):
                        os.remove(old_instance.branch_image.path)
            except Branch.DoesNotExist:
                pass
        super().save(*args, **kwargs)


class OpeningHour(models.Model):
    DAYS_OF_WEEK = [
        ('MO', 'Monday'),
        ('TU', 'Tuesday'),
        ('WE', 'Wednesday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday'),
        ('SA', 'Saturday'),
        ('SU', 'Sunday'),
        ('CL', 'Closed'),
    ]

    branch = models.ForeignKey(
        Branch, related_name='opening_hours', on_delete=models.CASCADE)
    day = models.CharField(max_length=2, choices=DAYS_OF_WEEK)
    open_time = models.TimeField(default='00:00')
    close_time = models.TimeField(default='23:59')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Ensure no duplicate days for the same branch
        unique_together = ('branch', 'day')

    def __str__(self):
        return f"{self.branch.branch_name} - {dict(self.DAYS_OF_WEEK).get(self.day)}: {self.open_time} to {self.close_time}"
