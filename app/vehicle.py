from abc import ABC, abstractmethod
from datetime import datetime

from app.receipt import ParkingReceipt
from app.enumerations import VehicleType
from app.ticket import ParkingTicket
from app.utils import Utils

util = Utils()

class Vehicle(ABC):
    def __init__(self) -> None:
        super().__init__()
        vehicle_type: VehicleType
        vehicle_number: str = ''
        ticket: ParkingTicket = None
        receipt: ParkingReceipt = None

    @abstractmethod
    def attach_ticket(self, spot_number: int):
        pass

    @abstractmethod
    def get_type(self):
        pass


class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.vehicle_type = VehicleType.car

    def get_type(self):
        return self.vehicle_type

    def attach_ticket(self, spot_number: int):
        ticket = ParkingTicket()
        ticket.generate(spot_number, util.current_time(), self.vehicle_type)
        self.ticket = ticket
        return ticket

class Truck(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.vehicle_type = VehicleType.truck

    def get_type(self):
        return self.vehicle_type

    def attach_ticket(self, spot_number: int):
        ticket = ParkingTicket()
        ticket.generate(spot_number, util.current_time(), self.vehicle_type)
        self.ticket = ticket
        return ticket

class Bus(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.vehicle_type = VehicleType.bus

    def get_type(self):
        return self.vehicle_type

    def attach_ticket(self, spot_number: int):
        ticket = ParkingTicket()
        ticket.generate(spot_number, util.current_time(), self.vehicle_type)
        self.ticket = ticket
        return ticket

class Scooter(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.vehicle_type = VehicleType.scooter
    
    def get_type(self):
        return self.vehicle_type

    def attach_ticket(self, spot_number: int):
        ticket = ParkingTicket()
        ticket.generate(spot_number, util.current_time(), self.vehicle_type)
        self.ticket = ticket
        return ticket

class Motorcycle(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.vehicle_type = VehicleType.motorcycle

    def get_type(self):
        return self.vehicle_type

    def attach_ticket(self, spot_number: int):
        ticket = ParkingTicket()
        ticket.generate(spot_number, util.current_time(), self.vehicle_type)
        self.ticket = ticket
        return ticket

class Suv(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.vehicle_type = VehicleType.suv

    def get_type(self):
        return self.vehicle_type

    def attach_ticket(self, spot_number: int):
        ticket = ParkingTicket()
        ticket.generate(spot_number, util.current_time(), self.vehicle_type)
        self.ticket = ticket
        return ticket


class VehicleFactory:
    def create(self, type: VehicleType):
        if type == VehicleType.car:
            return Car()
        elif type == VehicleType.bus:
            return Bus()
        elif type == VehicleType.truck:
            return Truck()
        elif type == VehicleType.motorcycle:
            return Motorcycle()
        elif type == VehicleType.suv:
            return Suv()
        elif type == VehicleType.scooter:
            return Scooter()
