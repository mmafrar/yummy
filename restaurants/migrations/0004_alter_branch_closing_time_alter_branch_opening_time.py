# Generated by Django 5.0.4 on 2024-05-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_branch_branch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='closing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='opening_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
