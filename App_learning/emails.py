from django.core.mail import send_mail
import random
from django.conf import settings
from .models import *

def send_otp(email):
    otp = random.randint(100000,999999)
    send_mail(
        'Your OTP for login',
        f'Your OTP for forget password is  {otp}',
        'laniyahiten1932@gmail.com',
        [email],
        fail_silently=False
    )
    user_obj = Student.objects.get(email_id = email)
    user_obj.otp = otp
    user_obj.save()