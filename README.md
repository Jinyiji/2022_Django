# hello world
1. startproject helloworld
   1. python -m pip install django~=3.2
   2. django-admin startproject helloworld
   3. python manage.py runserver
2. startapp
   1. python manage.py startapp playground
   2. settings.py > INSTALLED_APPS 'playground', 추가
3. playground/views
   1. say_hello()
4. urls
   1. playergroung/hello/ -> say_hello()