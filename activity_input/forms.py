from django import forms

from .models import Activity


class ActivityInputForm(forms.ModelForm):
    date = forms.DateField(label='Date (mm/jj/aaaa)')

    class Meta:
        model = Activity
        fields = [
            'title',
            'date',
            'description',
            'file'
        ]
