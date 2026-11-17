from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields= ('title','category','isbn', 'cost','year', 'published', 'cover')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control rounded-0'


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',  'password1', 'password2')

