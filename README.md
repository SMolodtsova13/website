# Веб-сайт для стоматологии


## Технологический стек
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
![Bootstrap](https://img.shields.io/badge/bootstrap-464646?style=flat&logo=bootstrap&logoColor=56C0C0&color=008080)
![Pandas](https://img.shields.io/badge/-pandas-464646?style=flat&logo=pandas&logoColor=56C0C0&color=008080)
![NumPy](https://img.shields.io/badge/-NumPy-464646?style=flat&logo=NumPy&logoColor=56C0C0&color=008080)


## Описание проекта 

Веб-сайт состит из двух страниц:  страница аутентификации и страница с информацией о приёмах, доступная только для зарегистрированного пользователей. Работа с данными ведется с помощью парсинга Excel таблиц с помощью DataFrame библиотеки Pandas.

Страница аутентификации. Осуществите аутентификацию пользователя используя файл auth.xlsx. 
Для нерарегитсрированных пользователей и при ошибке авторизации всплывает окно с ошибкой авторизации.

Страница отображения информации о приёмах.  
После авторизации пользователь перенаправляетсяна страницу с данными о его приёмах. На странице отображается баланс личного и семейного счетов, ФИО пользователя, филиалы клиник(в которых он был или записан в будущем) и информация о завершенных и будущих приема в клинике(дата и время приема, ФИО врача, количество дней до приема).

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

## Автор:  
_Молодцова Светлана_  
**telegram** _@smolodtsova_
