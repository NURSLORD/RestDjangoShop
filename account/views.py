import datetime
from datetime import timezone
from rest_framework import generics
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.serializers import UserSerializer
from shop.utils import own_send_email


class SendSmsToEmailView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        username = request.data['username']
        user = User.objects.filter(username=username, email=email)
        now = datetime.datetime.now(timezone.utc)
        if user:
            user = user[0]
            if (user.last_login and user.last_login + datetime.timedelta(minutes=1) < now) or user.last_login is None:
                user.last_login = now
                code = own_send_email(email)
                user.first_name = code
                user.save()
            else:
                return Response("Попробуйте через минуту!", status=400)
        else:
            code = own_send_email(email)
            new_user = User(username=username, email=email, last_login=now, first_name=code, is_active=True)
            new_user.save()
        return Response('Мы отправили вам код для подтверждения')


class LoginWithEmailView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data['email']
        code = request.data['code']
        user = User.objects.filter(email=email, first_name=code)
        if len(user) > 0 and len(user[0].first_name) > 3:
            user[0].first_name = ''
            user[0].save()
            token = Token.objects.filter(user=user[0])
            if token:
                token.delete()
            token = Token(user=user[0])
            token.save()
            return Response({
                'token': token.key,
                'user_pk': user[0].pk,
                'username': user[0].username
            })
        else:
            return Response({
                'error': "Неправильная пароль! "
            })


