from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

@api_view(['GET'])
# @permission_classes([IsAuthenticated, IsAdminUser])
def get_superusers(request):
    superusers = User.objects.filter(is_superuser=True)
    superuser_data = [
        {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        for user in superusers
    ]
    return Response(superuser_data)
