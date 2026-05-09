from django.urls import path  # type: ignore

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
