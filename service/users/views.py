from rest_framework.viewsets import ModelViewSet
from .models import ServiceUser
from .serializers import ServiceUserModelSerializer

# Create your views here.
class UserModelViewSet(ModelViewSet):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserModelSerializer
