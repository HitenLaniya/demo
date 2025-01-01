from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .emails import *
import re
# Create your views here.

#ADD STATE API
@api_view(['POST'])
def add_state(request):
    try:
        state = request.data.get("state_name")
        State.objects.create(state_name = state)
        return JsonResponse({'status': True,'msg':'State added successfully!!'})
    except:
        return JsonResponse({'status': True,'msg':'State not found!!'})


#DELETE STATE API
@api_view(['DELETE'])
def delete_state(request):
    try:
        id = request.data.get('id')
        state = State.objects.get(state_id = id)
        state.delete()
        return JsonResponse({'status': True, 'msg': 'State deleted successfully!!'})
    except:
        return JsonResponse({'status': True, 'msg': 'State Not Found!!'})

#UPDATE STATE API
@api_view(['POST'])
def update_state(request):
    try:
        id = request.data.get('id')
        state = State.objects.get(state_id = id)
        sname = request.data.get('state_name')
        state.state_name = sname
        state.save()
        return JsonResponse({'status':True,'msg':'State updated successfully!!'})
    except:
        return JsonResponse({'status':True,'msg':'State Not Found'})


#ADD STUDENT API
@api_view(['POST'])
def add_student(request):
    try:
        stu_name = request.data.get('student_name')
        mob_num = request.data.get('mobile_number')
        password = request.data.get('password')
        email = request.data.get('email_id')
        address = request.data.get('address')
        state = request.data.get('state_name')
        gender = request.data.get('gender')

        state_data = State.objects.get(state_name = state)

        Student.objects.create(
            student_name = stu_name,
            mobile_number = mob_num,
            email_id = email,
            address = address,
            state = state_data,
            password = password,
            gender = gender
        )
        return JsonResponse({'status':True,'msg':'Student details added successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})

#DELETE STUDENT API
@api_view(['DELETE'])
def delete_student(request):
    try:
        id = request.data.get('id')
        stu = Student.objects.get(student_id = id)
        stu.delete()
        return  JsonResponse({'status':True,'msg':'Student details deleted successfully!!'})
    except:
        return  JsonResponse({'status':True,'msg':'Student details Not Found!!'})

#UPDATE STUDENT API
@api_view(['POST'])
def update_student(request):
    try:
        id = request.data.get('id')
        stu = Student.objects.get(student_id = id)
        stu_name = request.data.get('student_name')
        mob_num = request.data.get('mobile_number')
        password = request.data.get('password')
        email = request.data.get('email_id')
        address = request.data.get('address')
        state = request.data.get('state_name')
        gender = request.data.get('gender')

        state_data = State.objects.get(state_name = state)
        stu.student_name = stu_name
        stu.mobile_number = mob_num
        stu.email_id = email
        stu.password = password
        stu.address = address
        stu.state = state_data
        stu.gender = gender

        stu.save()
        return JsonResponse({'status':True,'msg':'Student details updated successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Student details Not found!!'})
        

#ADD COURSE API
@api_view(['POST'])
def add_course(request):
    try:
        course = request.data.get('course_name')
        photo = request.data.get('thumbnail_url')
        # print(photo)
        Course.objects.create(
            course_name=course,
            thumbnail_url=photo)
        return JsonResponse({'status':True,'msg':'Course addedd successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'something went wrong!!'})

#DELETE COURSE API
@api_view(['DELETE'])
def delete_course(request):
    try:
        id = request.data.get('id')
        course = Course.objects.get(course_id = id)
        # print(course)
        course.delete()
        return JsonResponse({'status':True,'msg':'Course deleted successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})

#UPDATE COURSE API
@api_view(['POST'])
def update_course(request):
    try:
        id = request.data.get('id')
        course_obj = Course.objects.get(course_id = id)
        course = request.data.get('course_name')
        photo = request.data.get('thumbnail_url')

        course_obj.course_name = course
        course_obj.thumbnail_url = photo
        course_obj.save()
        return JsonResponse({'status':True,'msg':'Course updated successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})
    

#ADD SUBJECT API
@api_view(['POST'])
def add_subject(request):
    try:
        subject = request.data.get('subject_name')
        photo = request.data.get('thumbnail_url')
        course = request.data.get('course_name')

        course_data = Course.objects.get(course_name = course)
        Subject.objects.create(
            subject_name = subject,
            course = course_data,
            thumbnail_url = photo
        )
        return JsonResponse({'status':True,'msg':'Subject added successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})


#DELETE SUBJECT API
@api_view(['DELETE'])
def delete_subject(request):
    try:
        id = request.data.get('id')
        subject = Subject.objects.get(subject_id = id)
        subject.delete()
        return JsonResponse({'status':True,'msg':'Subject deleted successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})

#UPDATE SUBJECT API
@api_view(['POST'])
def update_subject(request):
    try:
        id = request.data.get('id')
        sub = Subject.objects.get(subject_id = id)
        subject = request.data.get('subject_name')
        photo = request.data.get('thumbnail_url')
        course = request.data.get('course_name')
        
        course_data = Course.objects.get(course_name = course)
        sub.subject_name = subject
        sub.thumbnail_url = photo
        sub.course = course_data
        sub.save()
        return JsonResponse({'status':True,'msg':'Subject updated successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})


#ADD TUTORIAL API
@api_view(['POST'])
def add_tutorial(request):
    try:
        tname = request.data.get('tutorial_name')
        tlink = request.data.get('tutorial_link')
        photo = request.data.get('thumbnail_url')
        subject = request.data.get('subject_name')
        # print(subject)
        subject_data = Subject.objects.get(subject_name = subject)
        print(subject_data)
        Tutorial.objects.create(
            tutorial_name = tname,
            tutorial_link = tlink,
            thumbnail_url = photo,
            subject = subject_data
        )
        return JsonResponse({'status':True,'msg':'Tutorial addedd successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})

#DELETE TUTORIAL API
@api_view(['DELETE'])
def delete_tutorial(request):
    try:
        id = request.data.get('id')
        tutorial = Tutorial.objects.get(tutorial_id = id)
        # print(tutorial)
        tutorial.delete()
        return JsonResponse({"status":True,'msg':'Tutorial deleted successfully!!'})
    except:
        return JsonResponse({'status':False,'msg':'Something went wrong!!'})

#UPDATE TUTORIAL API
@api_view(['POST'])
def update_tutorial(request):
    id = request.data.get('id')
    tutorial = Tutorial.objects.get(tutorial_id=id)
    tname = request.data.get('tutorial_name')
    tlink = request.data.get('tutorial_link')
    photo = request.data.get('thumbnail_url')
    subject = request.data.get('subject_name')

    subject_data = Subject.objects.get(subject_name = subject)

    tutorial.tutorial_name = tname
    tutorial.tutorial_link = tlink
    tutorial.thumbnail_url = photo
    tutorial.subject = subject_data
    tutorial.save()
    return JsonResponse({'status':True,'msg':'Tutorial updated successfully!!'})


#ADD QUESTION API
@api_view(['POST'])
def add_ques(request):
    que = request.data.get('question')
    op_a = request.data.get('option1')
    op_b = request.data.get('option2')
    op_c = request.data.get('option3')
    op_d = request.data.get('option4')
    right = request.data.get('right_ans')
    subject = request.data.get('subject')
    subject_data = Subject.objects.get(subject_name = subject)

    Question.objects.create(
        question = que,
        option_a = op_a,
        option_b = op_b,
        option_c = op_c,
        option_d = op_d,
        right_ans = right,
        subject = subject_data
    )
    return JsonResponse({'status':True,'msg':'Question added successfully!!'})

#DELETE QUESTION API
@api_view(['DELETE'])
def delete_ques(request):
    id = request.data.get('id')
    question = Question.objects.get(question_id = id)
    # print(question)
    question.delete()
    return JsonResponse({'status':True,'msg':'Question deleted successfully!!'})

#UPDATE QUESTION API
@api_view(['POST'])
def update_ques(request):
    id = request.data.get('id')
    question = Question.objects.get(question_id = id)
    que = request.data.get('question')
    op_a = request.data.get('option1')
    op_b = request.data.get('option2')
    op_c = request.data.get('option3')
    op_d = request.data.get('option4')
    right = request.data.get('right_ans')
    subject = request.data.get('subject')
    subject_data = Subject.objects.get(subject_name = subject)

    question.question = que
    question.option_a = op_a
    question.option_b = op_b
    question.option_c = op_c
    question.option_d = op_d
    question.right_ans = right
    question.subject = subject_data
    question.save()
    return JsonResponse({'status':True,'msg':'Question updated successfully!!'})

#ADD EXAM API
@api_view(['POST'])
def add_exam(request):
    ename = request.data.get('exam_name')
    subject = request.data.get('subject')
    subject_data = Subject.objects.get(subject_name =subject)

    Exam.objects.create(
        exam_name = ename,
        subject = subject_data
    )
    return JsonResponse({'status':True,'msg':'Exam added successfully!!'})

#DELETE EXAM API
@api_view(['DELETE'])
def delete_exam(request):
    id = request.data.get('id')
    exam =Exam.objects.get(exam_id = id)
    # print(exam)
    exam.delete()
    return JsonResponse({'status':True,'msg':'Exam deleted successfully!!'})

#UPDATE EXAM API
@api_view(['POST'])
def update_exam(request):
    id = request.data.get('id')
    exam =Exam.objects.get(exam_id = id)
    ename = request.data.get('exam_name')
    subject = request.data.get('subject')
    subject_data = Subject.objects.get(subject_name =subject)

    exam.exam_name = ename
    exam.subject = subject_data
    exam.save()
    return JsonResponse({'status':True,'msg':'Exam updates successfully!!'})


#ADD EXAM_CREATE API
@api_view(['POST'])
def add_create_exam(request):
    exam = request.data.get('exam_name')
    question = request.data.get('question')
    exam_data = Exam.objects.get(exam_name = exam)
    for que in question:
        temp_que = Question.objects.get(question_id = que)
        Create_Exam.objects.create(
            exam = exam_data,
            question = temp_que
        )
    return JsonResponse({'status':True,'msg':'questions are seleted'})

#DELETE EXAM_CREATE API
@api_view(['DELETE'])
def delete_create_exam(request):
    id = request.data.get('id')
    cexam = Create_Exam.objects.get(create_exam_id = id)
    # print(cexam)
    cexam.delete()
    return JsonResponse({'status':True,'msg':'Question deleted from exam paper!!'})

#in create_exam table there is no need change value if admin needs to change than remove that question and add whatever question that want from add_create_exam(api)(table)



#DELETE EXAM_ATTEMPT API
@api_view(['DELETE'])
def delete_attempt(request):
    stu_id = request.data.get('student_id')
    stu_obj = Student.objects.get(student_id = stu_id)
    exam_id = request.data.get('exam_id')
    exam_obj = Exam.objects.get(exam_id = exam_id)
    attempt = Exam_attempt.objects.filter(student = stu_obj)&Exam_attempt.objects.filter(exam = exam_obj)
    attempt.delete()
    res = Result.objects.filter(student = stu_obj)&Result.objects.filter(exam = exam_obj)
    print(res)
    res.delete()
    return JsonResponse({'status':True,'msg':'student attempt deleted for this exam'})


#DELETE RESULT API
@api_view(['DELETE'])
def delete_result(request):
    stu_id = request.data.get('student_id')
    stu_obj = Student.objects.get(student_id = stu_id)
    exam_id = request.data.get('exam_id')
    exam_obj = Exam.objects.get(exam_id = exam_id)
    res = Result.objects.filter(student = stu_obj)&Result.objects.filter(exam = exam_obj)
    # print(res)
    res.delete()
    return JsonResponse({'status':True,'msg':'Result deleted!!'})



#------------------------------------------------------------

#EXAM ATTEMPT AND RESULT GENERATE
# WHEN USER SUBMIT EXAM THAN CALL THIS API
#ATTEMPT EXAM API
@api_view(['POST'])
def attempt_exam(request):
    # exam = request.data.get('exam_id')
    answer = request.data.get('student_answer')
    create_exam = request.data.get('create_exam_id')
    student = request.data.get('student') #its come from session so need to convert this
    # exam_data = Exam.objects.get(exam_id = exam)
    stu = Student.objects.get(student_id = student)
    find_question = Create_Exam.objects.get(create_exam_id = create_exam)
    # print(find_question.exam)
    all_question = Create_Exam.objects.filter(exam = find_question.exam)
    # print(all_question)
    temp_ans = ""
    ans = []
    for i in answer:
        ans.append(i)
    for ques in all_question:
        for i in ans:
            temp_ans = i
            ans.pop(0)
            # print(temp_ans)
            break
        temp = Question.objects.get(question = ques.question)
        # print(temp.option_a)
        Exam_attempt.objects.create(
            student = stu,
            exam = find_question.exam,
            student_answers = temp_ans,
            question = temp.question,
            option_a = temp.option_a,
            option_b = temp.option_b,
            option_c = temp.option_c,
            option_d = temp.option_d,
            right_ans = temp.right_ans
        )
    
    # FOR RESULT count
    marks = 0
    result = Exam_attempt.objects.filter(exam = find_question.exam)& Exam_attempt.objects.filter(student= stu.student_id)
    print(result)
    for res in result:
        # print(res.right_ans)
        # print(res.student_answers)
        if str(res.right_ans) == str(res.student_answers):
            marks = int(marks) + 1
    # print(marks)
    Result.objects.create(
        student = stu,
        exam = find_question.exam,
        obtained_mark=marks
    )
    return JsonResponse({'status':True,'msg':'Found'})


# Statistics
#------------------------------------------------------------


@api_view(['POST'])
def login(request):
    email = request.data.get('email_id')
    password = request.data.get('password')
    students = Student.objects.all()
    for student in students:
        if str(student.email_id)== str(email):
            stu = Student.objects.get(email_id = email)
            if stu.password == password:
                send_otp(student.email_id)
                return JsonResponse({'status':True,'msg':'Student logged in'})
            else:
                return JsonResponse({'status':True,'msg':'Password not matching'})
        # print(students)
    return JsonResponse({'status':False,'msg':'Email is Not Registered!!'})


#OTP VERIFIFCATION
@api_view(['POST'])
def otp_verify(request):
    email = request.data.get('email_id')
    otp = request.data.get('otp')
    student = Student.objects.get(email_id = email)
    if str(student.otp) == otp:
        # redirect to main page
        request.session['email'] = email
        request.session['student_id'] = student.student_id
        return JsonResponse({'status':True,'msg':'OTP matched'})
    else:
        return JsonResponse({'status':True,'msg':'OTP Not matched'})
    

#SIGN UP API
@api_view(['POST'])
def signup(request):
    name = request.data.get('student_name')
    email = request.data.get('email_id')
    mob = request.data.get('mobile_number')
    password = request.data.get('password')
    confirm_pass = request.data.get('confirm_pass')
    students = Student.objects.filter(email_id = email)
    for student in students:
        if str(student.email_id) == email:
            return JsonResponse({'status':True,'msg':'Email id already exist please login'})
    
    if not password:
        return JsonResponse({'status':False,'msg':'password can not be empty!!'})
    if len(password)<8 or len(password)>16:
        return JsonResponse({'status':False,'msg':'password must be contain 8 to 16 character!!'})
    special_char = ['!','@','#','$','%','^','&','*']
    if(not any(char.islower() for char in password) or 
       not any(char.islower() for char in password) or
       not any(char.isdigit() for char in password) or
       not any(char in special_char for char in password)):
        return JsonResponse({'status':False,'msg':'Password must have uppercase, lowercase, digit and special character'})
    
   

    # if not any(char.islower() for char in password):
    #     return JsonResponse({'status':False,'msg':'Password must contain lower case!!'})
    # if not any(char.isupper() for char in password):
    #     return JsonResponse({'status':False,'msg':'Password must contain upper case!!'})
    # if not any(char.isdigit() for char in password):
    #     return JsonResponse({'status':False,'msg':'Password must contain numbers!!'})
    # special_char = ['!','@','#','$','%','^','&','*']
    # if not any(char in special_char for char in password):
    #     return JsonResponse({'status':False,'msg':'Password must contain Special character!!'})

    #this is shorctcut of password validation
    # if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()-+]).{8,16}$', password):
    #     return JsonResponse({'status':True,'msg':'Password must cotain capital and small letter, number and special character'})


    if str(password) == str(confirm_pass):
        Student.objects.create(
            student_name = name,
            email_id = email,
            mobile_number = mob,
            password = password
        )
        send_otp(email)
        return JsonResponse({'status':True,'msg':'Details registered success fully!!'})
    else:
        return JsonResponse({'status':True,'msg':'password not matched'})
    
#LOGOUT API
@api_view(['POST'])
def logout(request):
    print(request.session['email'])
    request.session['email'] = ""
    request.session['student_id'] = ""
    print(request.session['email'])
    return JsonResponse({'status':True,'msg':'Logged Out!!'})





#ADMIN 
#LOGIN
@api_view(['POST'])
def admin_login(request):
    emailId = request.data.get('emailId')
    password = request.data.get('password')
    admins = Admin.objects.filter(email_id = emailId)
    for admin in  admins:
        if str(admin.email_id) == emailId():
            # send_otp(emailId)
            pass
        else:
            return JsonResponse({'status':True,'msg':'Email id is not regestered'})


@api_view(['POST'])
def add_admin(request):
    pass