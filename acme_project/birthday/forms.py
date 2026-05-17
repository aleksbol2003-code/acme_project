from django import forms  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore

# Импортируем класс модели Birthday.
from .models import Birthday, Congratulation
# Импортируем функцию-валидатор.
from .validators import real_age

# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Применяем валидатор к полю birthday
    birthday = forms.DateField(
        validators=[real_age],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        # Указываем модель, на основе которой должна строиться форма
        model = Birthday
        # Указываем, что надо отобразить все поля
        # fields = '__all__'
        exclude = ('author',)

        def clean_first_name(self):
            # Получаем значение имени из словаря очищенных данных.
            first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
            return first_name.split()[0]

        def clean(self):
            # Вызов родительского метода clean.
            super().clean()
            # Получаем имя и фамилию из очищенных полей формы.
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            # Проверяем вхождение сочетания имени и фамилии во множество имён.
            if f'{first_name} {last_name}' in BEATLES:
                raise ValidationError(
                    'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
                )


class CongratulationForm(forms.ModelForm):

    class Meta:
        model = Congratulation
        fields = ('text',)
