from .models import *
from .globalFunc import *

def get_dialogs(name_user):
    user = get_user(name_user)
    dialogs = Сorrespondence.objects.raw(f'SELECT * FROM MessagerProject_сorrespondence WHERE users LIKE "%{user.id}%"')
    if len(dialogs) == 0:
        return 'you haven`t dialog'
    return dialogs

def create_dialog(name_user):
    user = get_user(name_user)
    create(Сorrespondence, users=user.id)
    return get_dialogs(name_user)

def get_message(id_group):
    pass


def get_user(name_user):
    users = User.objects.filter(name=name_user)
    if len(users) > 0:
        return users[0]
    return create(User, name=name_user)
     