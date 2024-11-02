import pandas as pd
import numpy as np
import locale
from datetime import datetime

from django.shortcuts import render, redirect

from backend.forms import LoginForm
from website.settings import BASE_DIR

locale.setlocale(locale.LC_ALL, '')


auth_data = pd.read_excel(BASE_DIR / 'backend/data/auth.xlsx')

receptions = pd.read_excel(
    BASE_DIR / 'backend/data/receptions.xlsx'
    ).fillna(pd.NaT)

def prepare_date(df):
    """Подготовка данных из таблицы receptions.xlsx"""
    date_columns = ['add_time', 'start_time', 'end_time', 'cancel_time']
    string_columns = ['phone', 'clinic', 'doctor_fio', 'patient_fio']
    integer_columns = ['id', 'patient_id', 'doctor_id', 'personal_account', 'family_account']

    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    for col in string_columns:
        df[col] = df[col].astype(str)

    for col in integer_columns:
        df[col] = df[col].fillna(0).astype(int)

    if 'card_comment' in df.columns:
        del df['card_comment']

    if 'reception_comment' in df.columns:
        del df['reception_comment']

    now = datetime.now().date()
    df['days_count'] = abs(((df['end_time'].dt.date - now) / np.timedelta64(1, 'D')).astype(int))
    return df

receptions = prepare_date(receptions)


def index(request):
    """Личный кабинет с данными о пользователе."""
    is_auth = request.session.get('is_auth', False)
    if is_auth is False:
        return redirect('backend:login')
    user_id = int(request.session['patient_id'])
    receptions_user = receptions.query('patient_id == @user_id')
    patient_fio = receptions_user['patient_fio'].values[0]
    personal_account = receptions_user['personal_account'].values[0]
    family_account = receptions_user['family_account'].values[0]

    now = datetime.now().date()

    future_visits = []
    finish_visits = []
    clinics = []
    for i, visit in receptions_user.iterrows():
        clinic = visit['clinic']
        doctor_fio = visit['doctor_fio']
        days_count = visit['days_count']
        start_time = visit['start_time']
        end_time = pd.to_datetime(visit['end_time']).time()

        if clinic not in clinics:
            clinics.append(clinic)

        visit_data = {
            'doctor_fio': doctor_fio,
            'days_count': days_count,
            'visit_time': start_time.strftime('%d %b (%a) %H:%M') + '-' + end_time.strftime('%I:%M'),
        }

        if start_time.date() < now:
            finish_visits.append(visit_data)
        else:
            future_visits.append(visit_data)

    return render(
        request, 'backend/index.html',
        {
            'clinics': clinics,
            'patient_fio': patient_fio,
            'is_auth': is_auth,
            'personal_account': personal_account,
            'family_account': family_account,
            'finish_visits': finish_visits,
            'future_visits': future_visits
        }
    )


def login(request):
    """Функция входа в аккаунт."""
    with_error = False
    form = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = int(form.cleaned_data['login'])
            password = form.cleaned_data['password']
            users = auth_data.query('login == @login & password == @password')

            if len(users) > 0:
                user_id = users['patient_id'].values[0]
                request.session['patient_id'] = str(user_id)
                request.session['login'] = str(login)
                request.session['password'] = password
                request.session['is_auth'] = True

                return redirect('backend:index')
            with_error = True

    else:
        form = LoginForm()

    return render(
        request, 'registration/login.html', {'form': form, 'with_error': with_error, 'is_auth': False}
    )

def logout(request):
    """Функция выхода из аккаунта."""
    request.session['patient_id'] = ''
    request.session['login'] = ''
    request.session['password'] = ''
    request.session['is_auth'] = False
    return redirect('backend:login')
