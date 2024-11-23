from django.contrib.auth import login
from rest_framework import permissions, throttling
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import views
from authentication.serializers import RegisterSerilaizer, UserSerializer
from rest_framework.response import Response
from knox.models import AuthToken

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    throttle_classes = (throttling.AnonRateThrottle,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        serializer=RegisterSerilaizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()

        return Response({
            "user":UserSerializer(user).data,
            "token":AuthToken.objects.create(user)[1]
        })