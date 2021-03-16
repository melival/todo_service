from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ServiceUser


class ServiceUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ServiceUser
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
