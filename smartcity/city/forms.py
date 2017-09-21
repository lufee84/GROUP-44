from django import forms
from city.models import Post


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a feedback'
        }
    ))

    class Meta:
        model = Post
        fields = ('post', )