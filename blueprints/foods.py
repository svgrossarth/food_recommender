import logging
from uuid import UUID
from flask import Blueprint, Response, jsonify, make_response, request
from werkzeug.exceptions import BadRequest
from mongoengine.errors import FieldDoesNotExist
from errors.validation_errors import ValidationError

from models.food import FoodItem
from validation.food_item_validation import validate_food_item

foods = Blueprint('foods', __name__)

logger = logging.getLogger(__name__)

@foods.route('/api/<int:version>/<uuid:user_id>/foods', methods=['GET'])
def get_foods(version, user_id) -> Response:
    food_items = FoodItem.objects(user_id=user_id)
    # TODO: I am not in love with json response. Update later.
    if len(food_items) != 0:
        return Response(food_items.to_json(), mimetype='application/json')
    else:
        logger.error(f'User: {user_id} does not have any food items.')
        return make_response(f'User: {user_id} does not have any food items.', 404)


@foods.route('/api/<int:version>/<uuid:user_id>/foods/<uuid:food_id>', methods=['GET'])
def get_food(version, user_id, food_id) -> Response:
    try:
        food_item = FoodItem.objects.get(food_id=food_id)
        # TODO: I am not in love with json response. Update later.
        return Response(food_item.to_json(), mimetype='application/json')
    except FoodItem.DoesNotExist as e:
        logger.exception(f'Food does not exist: {e}')
        return make_response(f'Food with food_id: {food_id} does not exist.', 404)
    

@foods.route('/api/<int:version>/<uuid:user_id>/foods', methods=['POST'])
def create_food(version: int, user_id: UUID) -> Response:
    try:
        food_item = validate_food_item(request, user_id)
        saved_food = food_item.save()
        response = jsonify({"food_id": saved_food.food_id})
        response.status_code = 201
        return response
    except ValidationError as e:
        logger.exception(f'Validation error: {e}')
        return make_response(e.error_response(), 400)
    except FieldDoesNotExist as e:
        logger.exception(f'Mongo Engine error: {e}')
        return make_response(f'Invalid input JSON input', 400)
    except BadRequest as e:
        logger.exception(f'Werkzeug Bad Request: {e}')
        return make_response(e.description, 400)

@foods.route('/api/<version>/<user_id>/foods/<food_id>', methods=['PATCH'])
def update_food(version, user_id, food_id):
    # Capture food_id from URL and data from request body
    update_data = request.json  # Assuming JSON data is sent
    # TODO: Implement logic to update a food and return the new complete food
    pass
