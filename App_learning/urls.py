from django.urls import path
from .views import *
urlpatterns = [
    #STATE
    path('add_state/',view=add_state,name='add_state'),
    path('delete_state/',view=delete_state,name='delete_state'),
    path('update_state/',view=update_state,name='update_state'),

    #STUDENT
    path('add_student/',view=add_student,name='add_student'),
    path('delete_student/',view=delete_student,name='delete_student'),
    path('update_student/',view=update_student,name='update_student'),

    #COURSE
    path('add_course/',view=add_course,name='add_course'),
    path('delete_course/',view=delete_course,name='delete_course'),
    path('update_course/',view=update_course,name='update_course'),

    #SUBJECT
    path('add_subject/',view=add_subject,name='add_subject'),
    path('delete_subject/',view=delete_subject,name='delete_subject'),
    path('update_subject/',view=update_subject,name='update_subject'),

    #TUTORIAL
    path('add_tutorial/',view=add_tutorial,name='add_tutorial'),
    path('delete_tutorial/',view=delete_tutorial,name='delete_tutorial'),
    path('update_tutorial/',view=update_tutorial,name='update_tutorial'),

    #QUESTION
    path('add_ques/',view=add_ques,name='add_ques'),
    path('delete_ques/',view=delete_ques,name='delete_ques'),
    path('update_ques/',view=update_ques,name='update_ques'),

    #EXAM
    path('add_exam/',view=add_exam,name='add_exam'),
    path('delete_exam/',view=delete_exam,name='delete_exam'),
    path('update_exam/',view=update_exam,name='update_exam'),

    #CREATE_EXAM
    path('add_create_exam/',view=add_create_exam,name='add_create_exam'),
    path('delete_create_exam/',view=delete_create_exam,name='delete_create_exam'),
    # path('update_create_exam/',view=update_create_exam,name='update_create_exam'),

    #ATTEMPT_EXAM
    path('delete_attempt/',view=delete_attempt,name='delete_attempt'),

    #RESULT
    path('delete_result/',view=delete_result,name='delete_result'),

    # USER BASED
    #ATTEMPT EXAM AND RESULT 
    path('attempt_exam/',view=attempt_exam,name='attempt_exam'),

    #SIGNUP
    path('signup/',view=signup,name='signup'),

    #LOGIN
    path('login/',view=login,name='login'),

    #LOGOUT
    path('logout/',view=logout,name='logout'),

    #OTP VERIFICATION
    path('otp_verify/',view=otp_verify,name="otp_verify"),



    #ADMIN 
    path('add_admin/',view=add_admin,name='add_name'),
]

