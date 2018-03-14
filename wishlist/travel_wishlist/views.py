from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.


def place_list(request): ##Handles requests for the home page

    ##Gets the data from the database with POST method and displays it in the view
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)  #Creates a place object
        place = form.save()
        if form.is_valid():
            place.save() #Saves the place to the database
            return redirect('place_list') #Redirects a get request

    ##Filters objects that have the boolean visted as false if request was not a post. Then orders it by name
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() #Creates a new form object
    ##Rendered as HTML
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'new_place_form' : new_place_form})

##Gets the places visited from the database with POST method and displays it in the view
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited' : visited})


def place_is_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')

