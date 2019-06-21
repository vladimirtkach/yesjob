# yesjob

### Быстрый старт

    1. Создайте и активируйте venv c python 3.6
    2. pip install -r requirements.txt
    3. Создайте базу данных yesjob на сервере mysql
    4. Создайте копию файла src/yesjob/settings/local.sample.env под именем local.env
    5. Пропишите в local.env свои логин и пароль к базе данных
    6. В папке src `python manage.py migrate`
    7. python manage.py runserver


