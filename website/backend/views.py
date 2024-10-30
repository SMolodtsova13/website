import pandas as pd
from datetime import datetime


from django.shortcuts import render



auth_data = pd.read_excel('auth.xlsx')



df = pd.read_excel('receptions.xlsx')

# Преобразуем столбцы к нужным типам
date_columns = ['date_of_reception']
string_columns = ['phone_number', 'clinic_name']
integer_columns = ['patient_id', 'status']

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

for col in string_columns:
    df[col] = df[col].astype(str)

for col in integer_columns:
    df[col] = df[col].fillna(-1).astype(int)



df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

   # Устанавливаем типы данных
types_map = {
       'patient_id': int,
       'name': str,
       'phone_number': str
}
for col, dtype in types_map.items():
       df[col] = df[col].astype(dtype)
   