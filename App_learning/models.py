from django.db import models

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    password = models.CharField(max_length=50,null=True)
    email_id = models.EmailField()
    otp= models.CharField(max_length=6,null=True)
    address = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE,default=1)
    gender_choice = (
        ('M','Male'),
        ('F','Female')
    )
    gender = models.CharField(choices=gender_choice,max_length=6)

    def __str__(self):
        return self.student_name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=20)
    thumbnail_url = models.ImageField(upload_to="uploads/", max_length=200)


    def __str__(self):
        return self.course_name
    
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=25)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    thumbnail_url = models.ImageField(upload_to="uploads/", max_length=200)


    def __str__(self):
        return self.subject_name

class Tutorial(models.Model):
    tutorial_id = models.AutoField(primary_key=True)
    tutorial_name = models.CharField(max_length=200)
    tutorial_link = models.CharField(max_length=200)
    thumbnail_url = models.ImageField(upload_to="uploads/", max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.tutorial_name

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=150)
    option_a = models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    option_d = models.CharField(max_length=50)
    right_ans = models.CharField(max_length=10)

    def __str__(self):
        return self.question
    
class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=25)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.exam_name

class Create_Exam(models.Model):
    create_exam_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.create_exam_id)

class Exam_attempt(models.Model):
    attemp_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
    # create_exam = models.ForeignKey(Create_Exam, on_delete=models.CASCADE, null=True)
    student_answers = models.CharField(max_length=10)
    question = models.CharField(max_length=150,null=True)
    option_a = models.CharField(max_length=50,null=True)
    option_b = models.CharField(max_length=50,null=True)
    option_c = models.CharField(max_length=50,null=True)
    option_d = models.CharField(max_length=50,null=True)
    right_ans = models.CharField(max_length=10,null=True)
    def __str__(self):
        return str(self.attemp_id)

class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
    obtained_mark = models.IntegerField()

    def __str__(self):
        return str(self.result_id)



class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.admin_name