from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Blog,Category
from .serializers import CategorySerializer,BlogSerializer
from .permissions import IsAdminOrReadOnly


class CatagoryModelViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ["name"]
    search_fields = ["name"]
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]


class BlogModelViewSet(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ["category"]
    search_fields = ["title","content"]
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]

