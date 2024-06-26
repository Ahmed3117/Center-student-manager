# Generated by Django 4.2.4 on 2024-05-27 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ActiveStudentnumbers', models.IntegerField()),
                ('monthCount', models.IntegerField()),
                ('session_teacher_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('session_center_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('session_total_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('month_teacher_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('month_center_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('month_total_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.center')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('register_date', models.DateField(auto_now_add=True)),
                ('paid_status', models.IntegerField()),
                ('current_status', models.IntegerField()),
                ('teacher_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('no_paid', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.class')),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MainBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField()),
                ('paid_type', models.CharField(max_length=50)),
                ('paid_status', models.IntegerField()),
                ('total_before', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_discount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_discount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_after', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_paid', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_paid', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_remain', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_remain', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_remain', models.DecimalField(decimal_places=2, max_digits=18)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_num', models.CharField(max_length=20)),
                ('parent_phone', models.CharField(max_length=20)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('code', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('block', models.BooleanField(default=False)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.division')),
            ],
        ),
        migrations.CreateModel(
            name='SalesBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField()),
                ('paid_type', models.CharField(max_length=50)),
                ('paid_status', models.IntegerField()),
                ('total_before', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_discount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_discount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_after', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_fee', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_paid', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_paid', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_remain', models.DecimalField(decimal_places=2, max_digits=18)),
                ('center_remain', models.DecimalField(decimal_places=2, max_digits=18)),
                ('teacher_remain', models.DecimalField(decimal_places=2, max_digits=18)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.mainbill')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('month_num', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.class')),
            ],
        ),
        migrations.AddField(
            model_name='mainbill',
            name='month_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.month'),
        ),
        migrations.CreateModel(
            name='Course_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('total_students', models.IntegerField()),
                ('attend', models.IntegerField()),
                ('absence', models.IntegerField()),
                ('count', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('status', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.class')),
                ('month_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.month')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.student'),
        ),
        migrations.AddField(
            model_name='class',
            name='division_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.division'),
        ),
        migrations.AddField(
            model_name='class',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.subject'),
        ),
        migrations.CreateModel(
            name='Attendance_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('out_attend', models.IntegerField()),
                ('notes', models.CharField(max_length=255)),
                ('home_work', models.IntegerField()),
                ('video_view', models.IntegerField()),
                ('teacher_paid_status', models.IntegerField()),
                ('course_attend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.course_attendance')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Absence_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('permission', models.IntegerField()),
                ('notes', models.CharField(max_length=255)),
                ('course_attend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.course_attendance')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.student')),
            ],
        ),
    ]
