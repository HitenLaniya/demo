# Generated by Django 5.1.4 on 2024-12-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_learning', '0009_remove_exam_attempt_create_exam_exam_attempt_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_attempt',
            name='question',
            field=models.CharField(max_length=150, null=True),
        ),
    ]