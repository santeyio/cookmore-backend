import django
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
#  from rest_framework.compat import authenticate


##################################################################
## Rewrite of rest_framework.authtoken.serializers.AuthTokenSerializer
##  to use email instead of username
##################################################################

def authenticate(request=None, **credentials):
    from django.contrib.auth import authenticate
    if django.VERSION < (1, 11):
        return authenticate(**credentials)
    else:
        return authenticate(request=request, **credentials)

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
