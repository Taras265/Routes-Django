from django import forms
from cities.models import City
from route.models import Route

from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='З міста', queryset=City.objects.all(),
                                       widget=forms.Select
                                       (attrs=
                                        {'class': 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label='У місто', queryset=City.objects.all(),
                                     widget=forms.Select(
                                         attrs=
                                         {'class': 'form-control js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(label='Через міста', queryset=City.objects.all(),
                                            widget=forms.SelectMultiple
                                            (attrs=
                                             {'class': 'form-control js-example-basic-multiple'}))
    travel_times = forms.IntegerField(label='Час путівлі', widget=forms.NumberInput(attrs=
                                                                                    {'class': 'form-control',
                                                                                     'placeholder': 'Час їзди'}))

    class Meta:
        model = Route
        fields = ('from_city', 'to_city', 'cities', 'travel_times')


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Імя маршруту',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Маршрут'}))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(),
                                       widget=forms.HiddenInput())
    to_city = forms.ModelChoiceField(queryset=City.objects.all(),
                                     widget=forms.HiddenInput())
    trains = forms.ModelMultipleChoiceField(queryset=Train.objects.all(),
                                            widget=forms.SelectMultiple
                                            (attrs=
                                             {'class': 'form-control d-none'}))
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
