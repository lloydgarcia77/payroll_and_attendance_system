# Generated by Django 2.2.3 on 2020-02-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='emer_cont_pers',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='emer_cont_pers_cont_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
