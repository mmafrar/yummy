# Generated by Django 5.0.4 on 2024-05-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0003_alter_branch_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='day',
            field=models.ManyToManyField(blank=True, related_name='branches', to='branches.day'),
        ),
    ]