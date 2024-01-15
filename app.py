from blueprints.foods import foods
from blueprints.food_schedules import food_schedules
from mongoengine import connect

from flask import Flask
import logging


def setup_connection():
    connect('food_tracker')

def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    setup_connection()

    app.register_blueprint(foods)
    app.register_blueprint(food_schedules)

    return app