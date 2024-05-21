from django.db import models

# Create your models here.


class Menu(models.Model):
    STARTERS = 'Starters'
    SALADS = 'Salads'
    SPECIALTY = 'Specialty'

    CATEGORY_CHOICES = [
        (STARTERS, 'Starters'),
        (SALADS, 'Salads'),
        (SPECIALTY, 'Specialty'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='menu/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=STARTERS,
    )

    def __str__(self):
        return self.name + "-" + self.price + "-" + self.category