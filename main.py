from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
import io

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    return data
