# Импортируем настройки проекта.
from django.conf import settings  # type: ignore
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static  # type: ignore
from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

# MEDIA_URL = 'media/'

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    # В конце добавляем к списку вызов функции static.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 