# Generated by Django 5.1.4 on 2024-12-17 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_learning', '0003_rename_tumbnail_url_course_thumbnail_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_attempt',
            name='create_exam',
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam',
        ),
    ]