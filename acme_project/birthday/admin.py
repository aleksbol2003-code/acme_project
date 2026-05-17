from django.contrib import admin  # type: ignore

# Из модуля models импортируем модель Category...
from .models import Birthday
from .models import Tag


# class TagAdmin(admin.ModelAdmin):
    # list_display = ('name',)
    # search_fields = ('name',)
    # ordering = ('name',)

# ...и регистрируем её в админке:
admin.site.register(Birthday)
admin.site.register(Tag)
