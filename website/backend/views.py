import pandas as pd
from datetime import datetime

from django.shortcuts import render, redirect

from backend.forms import LoginForm


auth_data = pd.read_excel('C:/Dev/Тестовое стоматология/website/website/backend/data/auth.xlsx')

receptions = pd.read_excel('C:/Dev/Тестовое стоматология/website/website/backend/data/receptions.xlsx')

def index(request):
    is_auth = request.session.get('is_auth', False)
    if is_auth is False:
        return redirect('backend:login')
    user_id = request.session['patient_id']
    return render(request, 'backend/index.html')


def login(request):
    with_error = False
    form = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            # users = auth_data.query(f'login == @{login} & password == @{password}')
            users = auth_data.query("login == @login and password == @password")
            print(auth_data)
            print(users)

            if len(users) > 0:
                user_id = users['patient_id'].values[0]
                request.session['patient_id'] = user_id
                request.session['login'] = login
                request.session['password'] = password
                request.session['is_auth'] = True
                print('Nen')
                return redirect('backend:index')
            with_error = True
    
    else:
        form = LoginForm()

    return render(
        request, 'registration/login.html', {'form': form, 'with_error': with_error}
    )
