from blueprints.foods import foods
from blueprints.food_schedules import food_schedules

from flask import Flask
import logging


def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    app.register_blueprint(foods)
    app.register_blueprint(food_schedules)

    return app