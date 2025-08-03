# this file call is used to initialize the package
from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Additional configuration and setup can be done here
    return app