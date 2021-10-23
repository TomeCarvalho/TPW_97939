from django.http import HttpResponse
from django.shortcuts import render

import json
import os

# Create your views here.
from cv_project.settings import STATIC_ROOT


def cv(request, cvid):
    with open(f'{STATIC_ROOT}/json/{cvid}.json', 'r') as cv:
        params = json.load(cv)['eurocv']
        # params['foto'] = f'{STATIC_ROOT}/imgs/{params["foto"]}'
        print(f'{params=}')
        return render(request, 'eurocv.html', params)


def home(request):
    params = {'cvs': []}
    for filename in os.listdir(f'{STATIC_ROOT}/json'):
        print(f'{filename=}')
        with open(f'{STATIC_ROOT}/json/{filename}', 'r') as cv:
            j = json.load(cv)['eurocv']
            name = j['personalInfo']['name']
            # photo = f'{STATIC_ROOT}/{j["foto"]}'
            photo = j["foto"]
            preview = {
                'id': filename[:-5],
                'name': name,
                'photo': photo
            }
            params['cvs'].append(preview)
    print(f'{params=}')
    return render(request, 'home.html', params)
