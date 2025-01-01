from django.contrib import admin
from .models import * 
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display = ['state_name','state_id']
admin.site.register(State,StateAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name','email_id','mobile_number','password','student_id']
admin.site.register(Student, StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','course_id']
admin.site.register(Course,CourseAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name','subject_id']
admin.site.register(Subject,SubjectAdmin)

class TutorialAdmin(admin.ModelAdmin):
    list_display = ['tutorial_name','tutorial_id']
admin.site.register(Tutorial,TutorialAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','question_id']
admin.site.register(Question,QuestionAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['exam_name','exam_id']
admin.site.register(Exam,ExamAdmin)

class CreateExamAdmin(admin.ModelAdmin):
    list_display = ['exam','question','create_exam_id']
admin.site.register(Create_Exam,CreateExamAdmin)

class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ['student','exam','attemp_id','student_answers','right_ans']
admin.site.register(Exam_attempt,ExamAttemptAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ['result_id','student','obtained_mark']
admin.site.register(Result,ResultAdmin)