from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import RegisterSerializer


class RegisterCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"detail":"user logout"})