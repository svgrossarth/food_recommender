import logging
from flask import Blueprint, make_response, request
from werkzeug.exceptions import BadRequest
from mongoengine.errors import FieldDoesNotExist
from errors.validation_errors import ValidationError

from models.food import FoodItem
from validation.food_item_validation import validate_food_item

foods = Blueprint('foods', __name__)

logger = logging.getLogger(__name__)

@foods.route('/api/<version>/<user_id>/foods', methods=['GET'])
def get_foods(version, user_id):
    print(f'spencer here are the version and user_id let see if the reloading works it does!!!: {version} {user_id}')
    return 'spencer here are the version and user_id: {} {}'.format(version, user_id)

@foods.route('/api/<version>/<user_id>/foods/<food_id>', methods=['GET'])
def get_food(version, user_id, food_id):
    # Capture food_id, user_id, and version from URL path
    # TODO: Implement logic to return a specific food
    pass

@foods.route('/api/<version>/<user_id>/foods', methods=['POST'])
def create_food(version, user_id):
    try:
        food_item = validate_food_item(request)
    except ValidationError as e:
        logger.exception(f'Validation error: {e}')
        return make_response(e.error_response(), 400)
    except FieldDoesNotExist as e:
        logger.exception(f'Mongo Engine error: {e}')
        return make_response(f'Invalid input JSON input', 400)
    except BadRequest as e:
        logger.exception(f'Werkzeug Bad Request: {e}')
        return make_response(e.description, 400)
    return 'spencer here is the data is good', 200

@foods.route('/api/<version>/<user_id>/foods/<food_id>', methods=['PATCH'])
def update_food(version, user_id, food_id):
    # Capture food_id from URL and data from request body
    update_data = request.json  # Assuming JSON data is sent
    # TODO: Implement logic to update a food and return the new complete food
    pass
