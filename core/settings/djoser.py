DJOSER = {
    # переопределить методы для обработки создания, получения и изменения данных о пользователе
    'SERIALIZERS': {
        'user_create': 'api.serializers.RegistrationUserSerializer',
        'user': 'api.serializers.MeUserSerializer',
        'current_user': 'api.serializers.MeUserSerializer',
    },
}
