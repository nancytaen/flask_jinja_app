from flask import Flask, render_template
from flask_cors import CORS

from config import configObject


def create_app():
    # instantiate the app
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(configObject)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    # with app.app_context():
    #     app.register_blueprint(blueprint)

    @app.route('/')
    def hello_world():
        return "Hello world!"
    # def top_page():
    #     return render_template("index.html")

    # init_db()

    return app
