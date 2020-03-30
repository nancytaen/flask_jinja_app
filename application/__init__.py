from flask import Flask, render_template
from flask_cors import CORS

from config import configObject
from application.model.model import init_db
from application.views.user import user


def create_app():
    # instantiate the app
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(configObject)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    # register blueprints
    with app.app_context():
        app.register_blueprint(user)

    @app.route('/')
    def hello_world():
        return "Hello world!"
    # def top_page():
    #     return render_template("index.html")

    # instantiate db connection
    init_db()

    return app
