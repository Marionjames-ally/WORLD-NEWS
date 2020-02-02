from flask import Flask
from config import config_options


def create_app(config_name):
    app = Flask(__name__)

    # create the application configurations
    app.config.from_object(config_options[config_name])

    return app
