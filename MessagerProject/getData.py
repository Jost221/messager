from .models import *

def get_dialogs(id_user):
    #need hashing id user
    a = Сorrespondence.objects.raw(f'SELECT * FROM MessagerProject_сorrespondence WHERE users LIKE "%{id_user}%"')
    
    return a

def get_message(id_group):
    pass