# E-commerce Backend with Django

This repository contains the backend code for an E-commerce project built with Django.

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/) (3.8 or higher)
- [Pip](https://pip.pypa.io/en/stable/installation/)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/giriteja94495/Ecommerce-Backend-Django-.git
cd Ecommerce-Backend-Django-


#Create a virtual environment :

python -m venv venv

# TO activate :

source venv/bin/activate


#To install the requirements

pip install -r requirements.txt

#To migrate the models and data :


python manage.py migrate


#create an admin user for yourself to login into the db dashboard

python manage.py createsuperuser

run the development server :

python manage.py runserver



The project should now be running at http://localhost:8000/. 
You can access the Django admin page here 

 http://localhost:8000/admin , use your super user login you created earlier





