from random import randint

from django.conf import settings
from django.core.mail import send_mail


def own_send_email(email, name='User') -> str:
    code = str(randint(100000, 999999))
    send_mail(
        'YOUR PIN CODE',
        f"Dear {name} your pin code is {code}\nIf it's not you just ignore it!",
        settings.EMAIL_HOST_USER,
        [email],
    )
    return code