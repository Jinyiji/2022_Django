from django.urls import path

from playground import views

app_name = 'playground'

urlpatterns = [
    path('hello/', views.say_hello, name='playground_hello'),  # playground:hello
    path('hello_html/', views.say_hello_html, name='hello_html'),
    path('bye_html/', views.say_bye_html, name='bye')
]