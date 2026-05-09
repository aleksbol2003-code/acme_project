from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
]
