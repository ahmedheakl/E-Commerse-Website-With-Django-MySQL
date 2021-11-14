from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.forms.models import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from auctions.models import *
from django.contrib.auth.decorators import login_required

from .models import User

def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("activeListing"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("activeListing"))
    else:
        return render(request, "auctions/register.html")

def listing(request, listing_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    listing = Listing.objects.get(id = listing_id)
    added = request.user in listing.watchers.all()
    comments = listing.listing_comments.all()
    if request.method == "POST":
        newbid = int(request.POST.get('newbid'))
        # checking if the newbid is greater than or equal to current bid
        if listing.startbid >= newbid:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "message": "Your Bid should be higher than the Current one.",
                "comments": comments,
                'added': added
            })
        # if bid is greater then updating in Listings table
        else:
            listing.startbid = newbid
            listing.save()
            # saving the bid in Bid model
            obj = Bid()
            obj.user = request.user
            obj.auction = listing
            obj.offer = newbid
            obj.save()
            product = Listing.objects.get(id=listing_id)
            return render(request, "auctions/listing.html", {
                "listing": product,
                "message": "Your Bid is added.",
                "comments": comments,
                'added': added
            })
    
    return render(request, 'auctions/listing.html',{
        'listing' : listing,
        'comments':comments,
        'added': added
    })

            
    

def watchlist(request):
    products = request.user.watched_lisitings.all()
    empty = False
    if len(products) == 0:
        empty = True
    return render(request, "auctions/watchlist.html", {
        'message': 'This is your watch list.',
        "products": products,
        "empty": empty
    })

def addtowatchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user in listing.watchers.all():
        listing.watchers.remove(request.user)    
    else:
        listing.watchers.add(request.user)
    listing.save()
    return HttpResponseRedirect(reverse('watchlist'))
        
def newListing(request):
    if request.method == 'POST':
        newItem = Listing()
        newItem.title = request.POST['title']
        newItem.description = request.POST['description']
        newItem.startbid = request.POST['startbid']
        newItem.category = Category.objects.get(category = request.POST['category'])
        newItem.creator = request.user
        newItem.buyer = request.user        
        if request.POST['image_link']:
            newItem.image_link = request.POST['image_link']
        else:
            newItem.image_link = request.POST['https://www.aust-biosearch.com.au/wp-content/themes/titan/images/noimage.gif']
        newItem.save()
        products = Listing.objects.all()
        return render(request, 'auctions/activeListing.html',{
            'products': products

        })
    else:
        categories = Category.objects.all()
        return render(request, 'auctions/newListing.html',{
            'categories' : categories
        })
        
@login_required
def activeListing(request):
    products = Listing.objects.all()
    # checking if there are any products
    empty = False
    if len(products) == 0:
        empty = True
    return render(request, "auctions/activelisting.html", {
        "products": products,
        "empty": empty
    })

def addcomment(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    obj = Comment()
    obj.comment = request.POST.get("comment")
    obj.user = request.user
    obj.listing = listing
    obj.save()
    comments = listing.listing_comments.all()
    added = request.user in listing.watchers.all()
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "added": added,
        "comments": comments
    })