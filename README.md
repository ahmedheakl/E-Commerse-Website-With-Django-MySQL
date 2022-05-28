# E-Commerse-Website-With-Django-MySQL
A simple E-Commerce website using Django framework for backend and MySQL for the database with HTML, JavaScript, and CSS for the frontend. The website has the functionalities of logging in users, creating items to view for buyers, adding bids for each item, and users adding comments and reviews. The website handle user requests using APIs and store their data and items using MySQL.

# How to Use 
* Clone this repository into your PC
* Start the server by writing ```python manage.py runserver``` into your terminal
* In order to manipulate the database:
    - Modify the model schema in `models.py` file
    - Track the migrations by writing ```python manage.py migrate``` into the terminal
    - Apply the migrations by writing ```python manage.py makemigrations <app_name>``` into the terminal

# Project Structure & Samples
This a single-application (named auctions) project implemented using django framework. The application consists of multiple views for login, adding itesm, and viewing items. SQL database is used to store user data, items, comments, and bids implemented as models:
  - User Model: modeling and storing user data, i.e., username, password, and email. 
  - Category Model: abstract model for the items categories
  - Listing Model: modeling the items attributes, i.e., title, description, image, watchers, category, and buyers.
  - Bid Model: model schema for the bids data including the auction, ther user, and the offer
  - Comment Model: modeling each comment data 

Here are some samples for items images viewing, bids and prices, comments, listings process:

<p align='center'>
    <img width=400 src="https://github.com/ahmedheakl/E-Commerse-Website-With-Django-MySQL/blob/main/imgs/auctions_preview_1.png">
    <img width=400 src="https://github.com/ahmedheakl/E-Commerse-Website-With-Django-MySQL/blob/main/imgs/auctions_preview_2.png">
    <img width=400 src="https://github.com/ahmedheakl/E-Commerse-Website-With-Django-MySQL/blob/main/imgs/auctions_preview_3.png">
    <img width=400 src="https://github.com/ahmedheakl/E-Commerse-Website-With-Django-MySQL/blob/main/imgs/auctions_preview_4.png">  
</p>
