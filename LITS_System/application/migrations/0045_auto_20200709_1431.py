# Generated by Django 2.2.3 on 2020-07-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0044_auto_20200709_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceinfo',
            name='overtime',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
