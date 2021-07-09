from django import forms
from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Місто'}))

    class Meta:
        model = City
        fields = ('name',)
