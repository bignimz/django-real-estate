from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


def index(request):
    listings = Listing.objects.order_by('-id')[:6]
    context = {'listings': listings}
    return render(request, 'index.html', context)

# CRUD, Create, Read/Retrieve, Update and Delete list

# Read/Retrieve all listings
def Listing_List(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'listings.html', context)

# Read/Retrieve a single listing
def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {'listing': listing}
    return render(request, 'listing.html', context)

# Create listing
def listing_create(request):
    form = ListingForm()
    # Checking if the method is POST
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listings/')

    context = {'form': form}
    return render(request, 'create_listing.html', context)


# Update Listing
def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    # Checking if the method is POST
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'update_listing.html', context)
    

# Delete Listing
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')