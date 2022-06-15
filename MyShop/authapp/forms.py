from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import ShopUser
from django.forms import ValidationError

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',)


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ("username", 'first_name', 'last_name', 'email', "avatar", 'age')

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise ValidationError("Вы должны быть больше 18 лет!")
        return data
