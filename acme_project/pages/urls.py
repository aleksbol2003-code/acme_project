from django.urls import path  # type: ignore

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
]
