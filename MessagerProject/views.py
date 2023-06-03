from django.shortcuts import HttpResponse
from .getData import *

# Create your views here.
def list_dialog(request):
    data = get_dialogs(request.GET['id'])
    return HttpResponse(f'{data}')

def create(request):
    data = create_dialog(request.GET['id'])
    return HttpResponse(f'{data}')