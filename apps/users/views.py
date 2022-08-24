from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TokenSerializer


class TokenCreatedView(TokenObtainPairView):
    serializer_class = TokenSerializer

# TODO создать регистрацию пользователя, вход только по jwt
