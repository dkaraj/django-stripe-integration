# Generated by Django 3.0.7 on 2020-08-07 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("memberships", "0003_membership"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
