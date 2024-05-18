# Generated by Django 5.0.4 on 2024-05-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), (
                    'Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=150)),
                ('branch_address', models.CharField(max_length=200)),
                ('branch_contact', models.CharField(max_length=150)),
                ('branch_image', models.ImageField(blank=True,
                 null=True, upload_to='media/restaurants/')),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('day', models.ManyToManyField(
                    related_name='branches', to='branches.day')),
            ],
        ),
    ]