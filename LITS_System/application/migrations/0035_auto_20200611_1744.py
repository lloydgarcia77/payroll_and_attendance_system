# Generated by Django 2.2.3 on 2020-06-11 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0034_concerns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concerns',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_fk', to='application.PersonalInfo'),
        ),
        migrations.AlterField(
            model_name='concerns',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_fk', to='application.PersonalInfo'),
        ),
    ]
