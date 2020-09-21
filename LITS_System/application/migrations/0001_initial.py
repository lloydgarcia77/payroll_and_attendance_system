# Generated by Django 2.2.3 on 2020-09-18 01:06

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
            name='CutOffPeriodInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_file', models.FileField(upload_to='documents/%Y/%m/%d', verbose_name='Attendance .xlsx file')),
                ('cut_off_period', models.CharField(max_length=100, null=True, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeItenerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_filed', models.DateField(auto_now_add=True)),
                ('noted_by', models.CharField(blank=True, max_length=100, null=True)),
                ('checked_by', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('date_filed', models.DateField(auto_now_add=True)),
                ('noted_by', models.CharField(blank=True, max_length=100, null=True)),
                ('checked_by', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelephoneNumberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_telephone_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telephone_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_skills_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_id', models.CharField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images/', validators=[application.models.file_validator_image])),
                ('suffix', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('middle_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('education', models.CharField(blank=True, max_length=50, null=True)),
                ('experience', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.CharField(blank=True, max_length=50, null=True)),
                ('emer_cont_pers', models.CharField(blank=True, max_length=50, null=True)),
                ('emer_cont_pers_cont_no', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OvertimeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rendered', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=200)),
                ('re_sp_ot', models.CharField(choices=[('Regulary Day', 'Regulary Day'), ('Rest Day', 'Rest Day'), ('Special Day', 'Special Day')], default='Regulary Day', max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('product', models.CharField(max_length=200)),
                ('timeIn', models.CharField(max_length=100)),
                ('timeOut', models.CharField(max_length=100)),
                ('duration', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('overtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overtime', to='application.Overtime')),
            ],
        ),
        migrations.AddField(
            model_name='overtime',
            name='employee_overtime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_overtime', to='application.PersonalInfo'),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
                ('category', models.CharField(choices=[('Uploading File', 'Uploading File'), ('Delete Uploaded File', 'Delete Uploaded File'), ('Creating Payroll', 'Creating Payroll'), ('Updating Payroll Settings', 'Updating Payroll Settings'), ('Updating Profile', 'Updating Profile'), ('Updating Password', 'Updating Password'), ('New User Registration', 'New User Registration'), ('Deleting Employee', 'Deleting Employee'), ('Reply Concerns', 'Reply Concerns'), ('Creating Employee Transaction', 'Creating Employee Transaction'), ('Updating Employee Transaction', 'Updating Employee Transaction'), ('Deleting Employee Transaction', 'Deleting Employee Transaction'), ('Add', 'Add'), ('Delete', 'Delete')], default='Uploading File', max_length=150)),
                ('level', models.CharField(choices=[('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('error', 'error')], default='success', max_length=150)),
                ('public', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='not_receiver_fk', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='not_sender_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MobileNumberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_mobile_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('allowance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('reason', models.CharField(default='None', max_length=150)),
                ('employee_salary_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_salary_fk', to='application.PersonalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePayroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payroll_date', models.DateField(auto_now=True)),
                ('basic_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('allowance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('overtime_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('late_or_absences', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('salary_or_cash_advance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('gross_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('sss_premiums', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('philhealth_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('pagibig_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('withholding_tax', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('pagibig_loan', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('deducted_salary_cash_advance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_deduction', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('net_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('thirteenth_month_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('employee_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_payroll_fk', to='application.PersonalInfo')),
                ('payroll_cutoff_period', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_cutoff_fk', to='application.CutOffPeriodInfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLeaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_filed', models.DateField(auto_now_add=True)),
                ('department', models.CharField(default='None', max_length=150)),
                ('status', models.CharField(choices=[('Disapproved', 'Disapproved'), ('Approved', 'Approved')], default='Disapproved', max_length=150)),
                ('no_days', models.IntegerField()),
                ('inclusive_dates', models.CharField(max_length=100)),
                ('reasons', models.CharField(max_length=250)),
                ('classification_of_leave', models.CharField(choices=[('Others', 'Others'), ('Vacation Leave', 'Vacation Leave'), ('Maternity Leave', 'Maternity Leave'), ('Sick Leave', 'Sick Leave'), ('Paternity Leave', 'Paternity Leave'), ('Leave without pay', 'Leave without pay')], default='Others', max_length=100)),
                ('leave_credits', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('less_this_application', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('balance_as_of_this_date', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('noted_by', models.CharField(blank=True, max_length=100, null=True)),
                ('checked_by', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_leave_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_leave_fk', to='application.PersonalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeIteneraryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('timeIn', models.CharField(max_length=100)),
                ('timeOut', models.CharField(max_length=100)),
                ('reasons', models.CharField(max_length=250)),
                ('employee_itenerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_itenerary', to='application.EmployeeItenerary')),
            ],
        ),
        migrations.AddField(
            model_name='employeeitenerary',
            name='employee_itenerary_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_itenerary_fk', to='application.PersonalInfo'),
        ),
        migrations.CreateModel(
            name='Concerns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('date_filed', models.DateField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_fk', to='application.PersonalInfo')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_fk', to='application.PersonalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(blank=True, max_length=50, null=True)),
                ('company_tin', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('personal_tin', models.CharField(blank=True, max_length=50, null=True)),
                ('sss_number', models.CharField(blank=True, max_length=50, null=True)),
                ('pagibig', models.CharField(blank=True, max_length=50, null=True)),
                ('philhealth', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_company_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_week', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('date', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('time_in', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('time_out', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('late', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('undertime', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('overtime', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('has_itenerary', models.BooleanField(default=False)),
                ('has_leave', models.BooleanField(default=False)),
                ('overtime_category', models.CharField(choices=[('No Overtime', 'No Overtime'), ('Regular Day', 'Regular Day'), ('Rest Day', 'Rest Day')], default='No Overtime', max_length=100)),
                ('holiday', models.CharField(choices=[('Regulary Day', 'Regulary Day'), ('New Year’s Day', 'New Year’s Day'), ('Araw ng Kagitingan', 'Araw ng Kagitingan'), ('Maundy Thursday', 'Maundy Thursday'), ('Good Friday', 'Good Friday'), ('Labor Day', 'Labor Day'), ('Independence Day', 'Independence Day'), ('National Heroes’ Day', 'National Heroes’ Day'), ('Bonifacio Day', 'Bonifacio Day'), ('Christmas Day', 'Christmas Day'), ('Rizal Day', 'Rizal Day')], default='Regulary Day', max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('cut_off_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cut_off_period_fk', to='application.CutOffPeriodInfo')),
                ('employee_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_personal_info_fk', to='application.PersonalInfo')),
            ],
        ),
    ]
