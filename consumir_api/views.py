from django.shortcuts import render
from django.http import HttpResponse

import requests

def canales(request):
    response = requests.get('https://6454ff2ea74f994b334eff5e.mockapi.io/channels')
    canales = response.json()
    #print(canales)

    return render(request, 'index.html',{
        'message':'Listado de Canales',
        'canales':canales,
    })
#
# def canales(request):
#     response = requests.get('https://6454ff2ea74f994b334eff5e.mockapi.io/channels')
#     canales = response.json()
#     print(canales)
#     return HttpResponse(canales)