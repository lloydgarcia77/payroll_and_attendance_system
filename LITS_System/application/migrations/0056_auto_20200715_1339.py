# Generated by Django 2.2.3 on 2020-07-15 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0055_auto_20200714_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtimedetails',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
