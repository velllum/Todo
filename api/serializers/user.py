from djoser.serializers import UserCreateSerializer, UserSerializer


class RegistrationUserSerializer(UserCreateSerializer):
    """- djoser - переопределить создания """
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'username', 'last_name', 'first_name', 'password']


class MeUserSerializer(UserSerializer):
    """- djoser - переопределить получения """
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'username', 'last_name', 'first_name']
