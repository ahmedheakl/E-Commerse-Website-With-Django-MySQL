from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('newListing', views.newListing, name='newListing'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('addtowatchlist/<int:listing_id>', views.addtowatchlist, name='addtowatchlist'),
    path('listing/<int:listing_id>', views.listing, name='listing'),
    path("activeListing", views.activeListing, name="activeListing"),
    path("addcomment/<int:listing_id>", views.addcomment, name="addcomment")
]
