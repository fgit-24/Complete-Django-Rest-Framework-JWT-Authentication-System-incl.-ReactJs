import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from .utils import generate_opt



def generate_opt():
    """
    Generate a 6-digit OTP (One Time Password).
    """
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp


def send_code_to_user(email):
    Subject='One time passcode for email verification'
    opt_code=generateOpt()
    print(opt_code)
    user=User.objects.get(email=email)
    current_site="myAuth.com"
    email_body=f"Hi {user.first_name} thanks for signing up on {current_site} please verify your email with the \n one time passcode {otp_code}!"
    from_email=settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=opt_code)

    d_email=EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
    d_email.send(fail_silently=True)