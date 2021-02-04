from django import forms
from .models import test_data1


class test_form1(forms.ModelForm):
    class Meta:
        model = test_data1
        fields = ('username', 'textfield1')
        labels = {
            'username': 'ユーザー名',
            'textfield1': '入力1',
        }
        help_texts = {
            'username': 'ユーザー名',
            'textfield1': '自由入力',
        }