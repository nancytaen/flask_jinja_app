# flask_jinja_app
This is a basic skeleton flask app coherent with the application factory model.
The app includes database setup which utilizes sqlalchemy ORM and blueprints to organize views directory. 
This app is ideal for medium to large sized application, or for anyone who like their code to be neat and well organized.

## Cloning the repository
Anyone is free to clone this repository to estbablish a basic flask-jinja application setup.
Please first initialize virtualenv by:
```
python -m virtualenv venv
```
Then activate virtualenv, and install all packages listed in requirements.txt by
(shown is Windows command)
```
venv\activate\Scripts
pip install -r requirements.txt
```

Also note that you should modify .flaskenv file for your specific project configuration, and add database uri for the file to run.
The default configuration provided is in development mode.
