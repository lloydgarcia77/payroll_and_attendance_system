# Generated by Django 2.2.3 on 2020-07-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0052_auto_20200714_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overtime',
            name='departments',
        ),
        migrations.AddField(
            model_name='overtime',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
