from  django import forms
from .models import PostModel


class SearchForm(forms.Form):
    charfield=forms.CharField()
    integerfield=forms.IntegerField()
    boolenfield=forms.BooleanField()
    emailfield=forms.EmailField()
    decimalfield=forms.DecimalField()

    def clean_integerfield(self,*args,**kwargs):
        integerfield=self.cleaned_data.get("integerfield")
        if integerfield<10:
            raise forms.ValidationError("integerfield must be more than 10")
        return integerfield

    def clean_charfield(self, *args, **kwargs):
        charfield = self.cleaned_data.get("charfield")
        if len(charfield) < 10:
            raise forms.ValidationError("charfield must be more than 10")
        return charfield

class PostModalForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields={
            'title',
            'content'
        }