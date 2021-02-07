# FlaskWebApi
Flask Web API Using MongoDB MongoEngine, and Flask RESTful. 
Just few APIs are created for the restaurant system.

# Postman document link for API details
https://www.getpostman.com/collections/2c7ef337c8ada77d0abd

# Install different python version and create virtual environment

sudo add-apt-repository ppa:deadsnakes/ppa   
sudo apt-get update   
sudo apt install python3.6

sudo apt-get install python3.6-venv 
python3.6-dev python3.6 -m venv venv_name

# Import csv file in mongodb:
mongoimport -d restaurants -c meals --type csv --file /path/meal_data.csv --headerline

# Export mongodb collection as csv file
mongoexport -h localhost -d restaurants -c meals --type=csv --fields name,description,price,image_url -q '{}' --out meals_data.csv

  


