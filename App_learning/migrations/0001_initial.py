# Generated by Django 5.1.4 on 2024-12-17 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=20)),
                ('tumbnail_url', models.ImageField(max_length=200, upload_to='media/uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=150)),
                ('option_a', models.CharField(max_length=50)),
                ('option_b', models.CharField(max_length=50)),
                ('option_c', models.CharField(max_length=50)),
                ('option_d', models.CharField(max_length=50)),
                ('right_ans', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Create_Exam',
            fields=[
                ('create_exam_id', models.AutoField(primary_key=True, serialize=False)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.question')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('mobile_number', models.BigIntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.state')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('obtained_mark', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.create_exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.student')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_attempt',
            fields=[
                ('attemp_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_answers', models.CharField(max_length=10)),
                ('create_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.create_exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=25)),
                ('tumbnail_url', models.ImageField(max_length=200, upload_to='media/uploads/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.course')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.subject'),
        ),
        migrations.CreateModel(
            name='tutorial',
            fields=[
                ('tutorial_id', models.AutoField(primary_key=True, serialize=False)),
                ('tutorial_name', models.CharField(max_length=200)),
                ('tutorial_link', models.CharField(max_length=200)),
                ('tumbnail_url', models.ImageField(max_length=200, upload_to='media/uploads/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_learning.subject')),
            ],
        ),
    ]