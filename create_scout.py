from django.contrib.auth import get_user_model

User = get_user_model()
email = 'scout@futbolpulse.com'
password = 'ScoutPassword123!'

if not User.objects.filter(email=email).exists():
    User.objects.create_user(
        email=email,
        nombre_completo='Ojeador Principal',
        tipo_usuario='Scout',
        password=password
    )
    print("SCOUT_CREATED_SUCCESSFULLY")
else:
    user = User.objects.get(email=email)
    user.set_password(password)
    user.tipo_usuario = 'Scout'
    user.save()
    print("SCOUT_UPDATED_SUCCESSFULLY")
