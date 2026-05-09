from django.urls import path  # type: ignore

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.birthday, name='create'),
]
