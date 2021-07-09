"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from cities.views import cities, CityDeteilView, CreateCityView,\
    RefactorCityView, DeleteCityView, CityListView

urlpatterns = [
    path('', CityListView.as_view(), name='home'),
    path('deteil/<int:pk>/', CityDeteilView.as_view(), name='deteil'),
    path('create/', CreateCityView.as_view(), name='create'),
    path('refactor/<int:pk>/', RefactorCityView.as_view(), name='refactor'),
    path('delete/<int:pk>/', DeleteCityView.as_view(), name='delete'),
]
