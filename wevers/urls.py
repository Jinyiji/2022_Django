from django.urls import path

from wevers import views

app_name = 'wevers'

urlpatterns = [
    path('정국/', views.show_정국, name='정국'),
    path('태형/', views.show_태형, name='태형')
]