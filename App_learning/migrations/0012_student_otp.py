# Generated by Django 5.1.4 on 2024-12-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_learning', '0011_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otp',
            field=models.CharField(max_length=6, null=True),
        ),
    ]