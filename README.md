# Веб-сайт для стоматологии


## Технологический стек
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Pandas](https://pandas.pydata.org/static/img/pandas.svg-Pandas%20REST%20Framework-464646?style=flat&logo=Pandas&logoColor=56C0C0&color=008080)]

numpy
pandas



## Описание проекта 



Имеющиеся данные:  информация о приёмах пациентов и самих пациентах, информация об авторизации на сайте в незашифрованном виде. Приёмы включают в себя будущие приёмы, завершенные приёмы, отменённые приёмы.

Подготовка данных:
Считайте данные из файла receptions.xlsx и заполните ими DataFrame. 
Задайте типы столбцов (str, int или datetime). Каждый тип должен быть применён как минимум 1 раз.
Удалите столбцы со всеми комментариями.
Замените отсутствующие значения на пустоты.
Добавьте столбец, считающий для будущих приёмов количество дней до приёма, а для завершенных приёмов – количество дней, прошедших после приёма.

Веб-сайт:
Веб-сайт можно развернуть локально. Веб-сайт должен состоять из двух страниц:  страница аутентификации и страница с информацией о приёмах, доступная только для зарегистрированных пользователей.
Страница аутентификации. Осуществите аутентификацию пользователя используя файл auth.xlsx. Незарегистрированным пользователям отобразите всплывающее окно с ошибкой авторизации.
Страница отображения информации о приёмах. 
После авторизации перенаправьте пользователя на страницу с данными о его приёмах. Соответствие устанавливается по введенному номеру телефона (логин). Для отображения использовать шаблон template.html. В список клиник попадают все клиники, в которых пациент уже был, или куда записан в будущем. Если у пациента нет завершенных или будущих приёмов, то нужно убрать отсутствующий блок. 
Необходимо вести логирование всех попыток аутентификаций (успешных и неуспешных).



## Запуск проекта

- Клонируйте репозиторий с проектом на свой компьютер. В терминале из рабочей директории выполните команду:
```
git clone https://github.com/SMolodtsova13/website.git
```

- Установить и активировать виртуальное окружение

```
source /venv/bin/activate
```

- Установить зависимости из файла requirements.txt

```
python -m pip install --upgrade pip
```
- Обновить зависимости
```
pip install -r requirements.txt
```


### Выполните миграции:
```
python manage.py migrate
```

- В папке с файлом manage.py выполнить команду:
```
python manage.py runserver
```

- Создание супер пользователя(для доступа к админ панели)
```
python manage.py createsuperuser
```

## Автор:  
_Молодцова Светлана_  
**telegram** _@smolodtsova_