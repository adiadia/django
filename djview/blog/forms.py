from  django import forms
from .models import PostModel

class PostModalForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields={
            'title',
            'content'
        }