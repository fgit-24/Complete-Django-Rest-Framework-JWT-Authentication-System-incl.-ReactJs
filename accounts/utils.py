import random
from django.core.mail import EmailMessage

def generate_opt():
    """
    Generate a 6-digit OTP (One Time Password).
    """
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp


def send_code_to_user(email):
