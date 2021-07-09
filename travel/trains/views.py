from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from trains.models import Train
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from trains.forms import TrainForm

__all__ = (
    'TrainListView',
    'TrainDeteilView',
    'CreateTrainView',
    'RefactorTrainView',
    'DeleteTrainView',
)


class TrainListView(ListView):
    paginate_by = 15
    model = Train
    template_name = 'trains/home.html'


class TrainDeteilView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/deteil.html'


class CreateTrainView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Поїзд додан!"


class RefactorTrainView(SuccessMessageMixin,LoginRequiredMixin,  UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/refactor.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Поїзд відформован!"


class DeleteTrainView(LoginRequiredMixin, DeleteView):
    model = Train
    form_class = TrainForm
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поїзд видалин!')
        return self.post(request, *args, **kwargs)
