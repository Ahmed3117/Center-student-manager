# Generated by Django 5.0.6 on 2024-06-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0003_alter_absence_details_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
