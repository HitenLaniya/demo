# Generated by Django 5.1.4 on 2024-12-17 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_learning', '0007_exam_attempt_option_a_exam_attempt_option_b_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_attempt',
            name='exam',
        ),
    ]