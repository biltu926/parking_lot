from enum import Enum


class VehicleType(Enum):
    scooter = 1
    motorcycle = 2
    car = 3
    bus = 4
    suv = 5
    truck = 6

class ParkingType(Enum):
    mall = 1
    airport = 2
    stadium = 3

class ParkingSpotType(Enum):
    two_wheeler = 1
    car = 2
    bus = 3