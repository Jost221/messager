from .models import *
from .globalFunc import *

def get_dialogs(name_user):
    user = get_user(name_user)
    dialogs = Сorrespondence.objects.raw(f'SELECT * FROM MessagerProject_сorrespondence WHERE users LIKE "%{user.id}%"')
    if len(dialogs) == 0:
        return 'you haven`t dialog'
    return to_dict(dialogs)

def create_dialog(name_user, dialog):
    user = get_user(name_user)
    if len(Сorrespondence.objects.filter(name=dialog)) > 0:
        return 'Error'
    create(Сorrespondence, users=user.id, name=dialog)
    return get_dialogs(name_user)

def get_user(name_user):
    users = User.objects.filter(name=name_user)
    if len(users) > 0:
        return users[0]
    return create(User, name=name_user)

def connect_dialog(name_user, dialog):
    user = get_user(name_user)
    cor = Сorrespondence.objects.filter(name=dialog)[0]
    if str(name_user) not in cor.users:
        cor.users+=f' {user.id}'
        cor.save()
    return get_dialogs(name_user)

def get_message(user_name, dialog):
    dialog_dict = {} 
    status, dialog, user = check_in_cor(user_name, dialog)
    if status:
        messages = Message.objects.filter(correspondence=dialog)
        for i in range(len(messages)):
            dialog_dict[i] = {}
            dialog_dict[i]['user'] = User.objects.get(pk=messages[i].user_id).name
            dialog_dict[i]['text'] = messages[i].message
        return dialog_dict

def send_message(user_name, dialog, text):
    status, dialog_, user = check_in_cor(user_name, dialog)
    if status:
        create(Message, message=text, user=user, correspondence=dialog_)
        return get_message(user_name, dialog)

def check_in_cor(user_name, dialog):
    user = get_user(user_name)
    cor_list = Сorrespondence.objects.raw(f'SELECT * FROM MessagerProject_сorrespondence WHERE users LIKE "%{user.id}%"')
    necessary = Сorrespondence.objects.filter(name=dialog)
    if len(necessary) > 0 and necessary[0] in cor_list:
        return True, necessary[0], user
    return False, None, None