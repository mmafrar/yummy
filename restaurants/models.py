from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Day(models.TextChoices):
    MONDAY = 'MON', _('Monday')
    TUESDAY = 'TUE', _('Tuesday')
    WEDNESDAY = 'WED', _('Wednesday')
    THURSDAY = 'THU', _('Thursday')
    FRIDAY = 'FRI', _('Friday')
    SATURDAY = 'SAT', _('Saturday')
    SUNDAY = 'SUN', _('Sunday')


# class Day(models.Model):
#     day_of_week = models.CharField(max_length=150)

#     def __str__(self):
#         return self.day_of_week


class Branch(models.Model):
    branch_name = models.CharField(max_length=150)
    branch_address = models.CharField(max_length=200)
    branch_contact = models.CharField(max_length=150)
    branch_image = models.ImageField(
        upload_to='media/restaurants/', null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    # day = models.ForeignKey(Day, on_delete=models.CASCADE)
    day = models.CharField(
        max_length=3,
        choices=Day.choices,
        default=Day.MONDAY,
    )

    def is_closed(self):
        return self.opening_time is None and self.closing_time is None

    def __str__(self):
        return self.branch_name
