# Generated by Django 3.1.13 on 2022-08-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_management', '0018_auto_20220805_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='remarks',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]