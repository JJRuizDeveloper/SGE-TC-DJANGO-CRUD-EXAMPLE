from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm

def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})

def create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect(index)
    else:
        form = PokemonForm()
        return render(request, 'create.html', {'form': form})


def update(request, id):
   pokemon = Pokemon.objects.get(id=id)
   if request.method == 'POST' or request.method == 'PUT':
       form = PokemonForm(request.POST, instance=pokemon)
       if form.is_valid:
           form.save()
       return redirect(index)
   else:
       form = PokemonForm(instance=pokemon)
       return render(request, 'update.html', {'form': form})


def delete(request,id):
    if request.method == 'POST' or request.method == 'DELETE':
        pokemon = Pokemon.objects.get(id=id)
        pokemon.delete()
        return redirect(index)
