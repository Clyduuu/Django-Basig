"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from CardGame.views import HomePageView, TrainerListView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView, CollectionListView, CollectionCreateView, CollectionUpdateView, CollectionDeleteView, PokemonCardListView, PokemonCreateView, PokemonUpdateView, PokemonDeleteView

from CardGame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerListView.as_view(), name='trainer-list'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete',TrainerDeleteView.as_view(), name='trainer-delete'),
    path('collection_list', CollectionListView.as_view(), name='collection-list'),
    path('collection_list/add', CollectionCreateView.as_view(), name='collection-add'),
    path('collection_list/<pk>', CollectionUpdateView.as_view(), name='collection-update'),
    path('collection_list/<pk>/delete',CollectionDeleteView.as_view(), name='collection-delete'),
    path('pokemoncard_list', PokemonCardListView.as_view(), name='pokemoncard-list'),
    path('pokemoncard_list/add', PokemonCreateView.as_view(), name='pokemon_add'),
    path('pokemoncard_list/<pk>', PokemonUpdateView.as_view(), name='pokemon_edit'),
    path('pokemoncard_list/<pk>/delete',PokemonDeleteView.as_view(), name='pokemon_del'),
    

]
