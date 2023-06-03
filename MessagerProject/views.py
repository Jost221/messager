from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .getData import *
import json

def get_CSRF(request):
    res = HttpResponse()
    res.set_cookie('biba', 5)
    return res


def list_dialog(request):
    data = json.loads(request.body)
    data = get_dialogs(data['name'])
    return HttpResponse(f'{data}')

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data = create_dialog(data['name'], data['dialog'])
        return HttpResponse(f'{data}')

@csrf_exempt
def connect(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        data = connect_dialog(data['name'], data['dialog'])
        return HttpResponse(f'{data}')
    
@csrf_exempt
def messages(request):
    data = json.loads(request.body)
    if request.method == 'GET':
        return HttpResponse(f'{get_message(data["name"], data["dialog"])}')
    elif request.method == 'POST':
        return HttpResponse(f'{send_message(data["name"], data["dialog"], data["message"])}')
