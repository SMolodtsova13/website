import pandas as pd
from datetime import datetime

from django.shortcuts import render, redirect

from backend.forms import LoginForm


auth_data = pd.read_excel('C:/Dev/Тестовое стоматология/website/website/backend/data/auth.xlsx')

receptions = pd.read_excel(
    'C:/Dev/Тестовое стоматология/website/website/backend/data/receptions.xlsx'
    )

def prepare_date(df):
    """Подготовка данных из таблицы receptions.xlsx"""
    date_columns = ['add_time', 'start_time', 'end_time', 'cancel_time']
    string_columns = ['phone', 'clinic', 'doctor_fio', 'patient_fio']
    integer_columns = ['id', 'patient_id', 'doctor_id', 'personal_account', 'family_account']

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    for col in string_columns:
        df[col] = df[col].astype(str)

    for col in integer_columns:
        df[col] = df[col].fillna(0).astype(int)
    
    if 'card_comment' in df.columns:
        del df['card_comment']

    if 'reception_comment' in df.columns:
        del df['reception_comment']

    now = datetime.now().date()
    new_df = df.assign(
        days_count = abs(df['end_time'].dt.date - now)
    )
    print(new_df)
    return new_df

receptions = prepare_date(receptions)


def index(request):
    is_auth = request.session.get('is_auth', False)
    if is_auth is False:
        return redirect('backend:login')
    user_id = int(request.session['patient_id'])
    login = request.session['login']

    receptions_user = receptions.query('patient_id == @user_id')
    print(receptions_user)
    personal_account = receptions_user['personal_account'].values[0]
    family_account = receptions_user['family_account'].values[0]
    
    now = datetime.now().date()

    future_visits = []
    finish_visits = []
    for i, visit in receptions_user.iterrows():
        doctor_fio = visit['doctor_fio']
        end_time = visit['end_time']
        if now > end_time:
            finish_visits.append(visit)
        future_visits.append(visit)




    return render(
        request, 'backend/index.html',
        {
            'login': login,
            'is_auth': is_auth,
            'personal_account': personal_account,
            'family_account': family_account
        }
    )


def login(request):
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
    request.session['patient_id'] = ''
    request.session['login'] = ''
    request.session['password'] = ''
    request.session['is_auth'] = False
    return redirect('backend:login')
    