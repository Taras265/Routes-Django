from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from route.forms import RouteForm
from route.find_routes import get_routes
from trains.models import Train
from cities.models import City
from route.forms import RouteModelForm
from route.models import Route

__all__ = (
    'RouteListView',
    'RouteDeteilView',
    'DeleteRouteView',
)


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, "Нема данних для поіска")
        return render(request, 'routes/home.html', {'form': form})


def create_route(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(initial={
                'from_city': cities[from_city_id],
                'to_city': cities[to_city_id],
                'travel_times': total_time,
                'trains': qs
            })
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, "Нема такого маршруту для збереження")
        return redirect('/')


def add_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Маршрут збережен")
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, "Нема такого маршруту для збереження")
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 15
    model = Route
    template_name = 'routes/list.html'


class RouteDeteilView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/deteil.html'


class DeleteRouteView(LoginRequiredMixin, DeleteView):
    model = Route
    form_class = RouteForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Маршрут видалин!')
        return self.post(request, *args, **kwargs)
