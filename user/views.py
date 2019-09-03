from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import CustomAuthTokenSerializer

## Override DRF AuthTokenSerializer with custom serializer
class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
