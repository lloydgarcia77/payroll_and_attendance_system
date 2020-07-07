# Generated by Django 2.2.3 on 2020-02-19 06:17

import application.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_id', models.CharField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images/', validators=[application.models.file_validator_image])),
                ('suffix', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('date_started', models.DateField()),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('education', models.CharField(blank=True, max_length=50, null=True)),
                ('experience', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
