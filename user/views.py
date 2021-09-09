from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        return None


    def perform_create(self, serializer):
        serializer.save()





