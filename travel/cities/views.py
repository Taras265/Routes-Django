from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from cities.models import City
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from cities.forms import CityForm
from django.urls import reverse_lazy

__all__ = (
    'cities',
    'CityDeteilView',
    'CreateCityView',
    'RefactorCityView',
    'DeleteCityView',
    'CityListView',
)


def cities(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    if pk:
        city = get_object_or_404(City, id=pk)
        context = {'object': city}
        return render(request, 'cities/deteil.html', context)
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 15)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/cities.html', context)


class CityDeteilView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/deteil.html'


class CreateCityView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Місто додано!"


class RefactorCityView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/refactor.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Місто відформовано!"


class DeleteCityView(LoginRequiredMixin, DeleteView):
    model = City
    form_class = CityForm
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Місто видалино!')
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 15
    model = City
    template_name = 'cities/cities.html'
