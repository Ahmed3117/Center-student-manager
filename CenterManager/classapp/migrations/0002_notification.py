# Generated by Django 4.2.4 on 2024-05-27 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.student')),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
    ]
