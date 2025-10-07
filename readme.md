# Django Marketplace

## Description
A fully functional **Marketplace Web Application** built using **Django**. This app allows users to sign up, browse
products, add listings, and make purchases. The app supports basic user authentication, product management, and a
shopping cart, simulating the essential features of an e-commerce marketplace.

## Technologies Used
- **Django**: A Python backend framework for web applications.
- **SQLite**: The database used to store user and product data.
- **HTML5/CSS3**: Used for creating the structure and styling of the frontend.
- **JavaScript**: For interactivity in the frontend (e.g., dynamic updating of cart and listings).
- **Tailwind CSS**: A CSS framework for responsive and mobile-first web design.
- **Git**: Version control for tracking changes in the project.

## Features
- **User Authentication**: Users can create accounts, log in, and log out.
- **Marketplace Listings**: Users can browse, add, edit, and delete product listings.
- **Product Search**: Search for products by name, category, or price range.
- **User Profiles**: Users can view and edit their profiles, and see their purchased products.
- **User Inbox**: Users can send messages to the sellers using the built-in messaging system.
- **Admin Interface**: An admin dashboard for managing users, products, and orders.

## Installation
To set up this project locally, follow the steps below:
### Prerequisites
**Python 3.x**
**Django 5.x.x**
**Git**
### Installation steps
- Clone the repository from https://github.com/toshevk/django-marketplace.git
- Create a python virtual environment
- Install requirements.txt
- Setup database (Currently the project is running the native SQLite3 database native to Django),
if you wish to use a different database such as PostreSQL, you can modify the DATABASES setting in settings.py
- Run database migrations using the command "python manage.py migrate"
- Create a Django Superuser to access the Admin panel using the command "python manage.py createsuperuser"
- Start the Development Server using the command "python manage.py runserver"
### Access the Application
- Once the development server is running, you can access the app at "http://127.0.0.1:8000"
- Once you have created the Superuser, you can access the Admin Panel at "http://127.0.0.1:8000/admin"

## Contributions
All contributions are welcome!
You are free to fork the repository and make changes to a new branch. Once you have made your changes,
you can commit and push to your fork. Opened pull requests will be reviewed as soon as possible.

## License
This project is open-source and available under the **MIT License**.

## Acknowledgements
- **Django** and the **Django REST Framework** for providing powerful tools for backend development that saved me A TON of time.
- **Tailwind CSS** for simplifying the front-end design process
- Inspiration from existing various marketplace and e-commerce apps
