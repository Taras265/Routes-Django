from django import forms
from trains.models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Номер', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Номер'}))
    travel_time = forms.IntegerField(label='Час путівлі', widget=forms.NumberInput(attrs=
                                                                        {'class': 'form-control',
                                                                         'placeholder': 'Час їзди'}))
    from_city = forms.ModelChoiceField(label='З міста', queryset=City.objects.all(),
                                       widget=forms.Select(attrs=
                                                           {'class': 'form-control'}))
    to_city = forms.ModelChoiceField(label='У місто', queryset=City.objects.all(),
                                     widget=forms.Select(attrs=
                                                         {'class': 'form-control'}))

    class Meta:
        model = Train
        fields = '__all__'
