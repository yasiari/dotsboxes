# -*- coding: utf-8 -*- 


from apps.auth.models import User


def authenticate(username=None, password=None):
    """
        User check password return User 
        authenticate(username=username, password=password) 
    """
    try:
        user = User.objects.get(username=username, is_active=True)
    except:
        user = None
    else: 
        if user and user.check_password(password):
            return user
    return None


def login(request, user):
    pass


def logout(request):
    pass
