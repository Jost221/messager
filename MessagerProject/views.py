from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .getData import *
import json

def get_CSRF(request):
    res = HttpResponse()
    res.set_cookie('biba', 5)
    return res


def list_dialog(request):
    data = request.GET
    data = get_dialogs(data['name'])
    return HttpResponse(f'{data}')

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = request.GET
        data = create_dialog(data['name'], data['dialog'])
        return HttpResponse(f'{data}')

@csrf_exempt
def connect(request):
    if request.method == 'PUT':
        data = request.GET
        data = connect_dialog(data['name'], data['dialog'])
        return HttpResponse(f'{data}')
    
@csrf_exempt
def messages(request):
    data = request.GET
    if request.method == 'GET':
        return HttpResponse(f'{get_message(data["name"], data["dialog"])}')
    elif request.method == 'POST':
        return HttpResponse(f'{send_message(data["name"], data["dialog"], data["message"])}')
    
@csrf_exempt
def log_out(request):
    data = request.GET
    if request.method == 'DELETE':
        return HttpResponse(f'{get_dialogs(data["name"])}')
