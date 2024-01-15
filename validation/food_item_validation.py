
import logging
from uuid import UUID
from flask import make_response, request
from mongoengine.errors import FieldDoesNotExist
from errors.validation_errors import InvalidJSON, InvalidJSONField, ValidationError

from models.food import FoodItem

logger = logging.getLogger(__name__)

def validate_food_item(request: request, user_id: UUID) -> FoodItem:

    if request.is_json is False:
        raise InvalidJSON('Request body is not JSON.')
    else:
        data = request.get_json()
    if 'columns' not in data or not isinstance(data['columns'], list):
        raise InvalidJSONField('Invalid or missing "columns" field in JSON data.')
    for column in data['columns']:
        if not isinstance(column, dict):
            raise InvalidJSONField('Invalid "column" field in JSON data.')

    food_time = FoodItem(**data)
    food_time.user_id = user_id
    logger.debug(f'Validated food item: {food_time}')
    return food_time