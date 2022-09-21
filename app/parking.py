from app import exceptions
from app.receipt import ParkingReceipt
from app.vehicle import Vehicle
from app.enumerations import ParkingSpotType, ParkingType, VehicleType
from app.fee_models import AirportFeeModel, FeeModel, MallFeeModel, StadiumFeeModel
from app.vehicle import VehicleFactory
from app.parking_spot import ParkingSpotFactory


class Parking:

    fee_model: FeeModel
    two_wheeler_spots: dict = {}
    car_spots: dict = {}
    truck_spots: dict = {}
    tickets: dict = {}

    def __init__(self, fee_model: FeeModel, 
                two_wheeler: int = 0, cars: int = 0,
                trucks: int = 0) -> None:
        Parking.fee_model = fee_model
        self.two_wheeler_spot_limit = two_wheeler
        self.car_spot_limit = cars
        self.truck_spot_limit = trucks

    def __repr__(self) -> str:
        return f'Fee model: {Parking.fee_model}\nTwo wheeler limit: {self.two_wheeler_spot_limit}\nCar limit: {self.car_spot_limit}\n Truck/Bus limit: {self.truck_spot_limit}'

    @classmethod
    def _set_fee_model(cls, fee_model):
        Parking.fee_model = fee_model
    
    def _available_car_spots(self):
        return len(self.car_spots)

    def _available_two_wheeler_spots(self):
        return len(self.two_wheeler_spots)

    def _available_truck_spots(self):
        return len(self.truck_spots)

    def parking_ticket(self, ticket_number: str):
        return Parking.tickets.get(ticket_number)

    def free_spot(self, type_: str, spot_number):
        if type_ in ['bus', 'truck']:
            Parking.truck_spots.pop(spot_number)
        elif type_ in ['scooter', 'motorcycle']:
            Parking.two_wheeler_spots.pop(spot_number)
        elif type_ in ['car', 'suv']:
            Parking.car_spots.pop(spot_number)
        else:
            pass

    def _assign_spot(self, vehicle: Vehicle, spot):
        if vehicle.get_type() in [VehicleType.car, VehicleType.suv]:
            if self._available_car_spots() >= self.car_spot_limit:
                raise exceptions.ParkingFull(f" Car parking is full. ")
            Parking.car_spots.update({spot._id(): spot})
        
        elif vehicle.get_type() in [VehicleType.scooter, VehicleType.motorcycle]:
            if self._available_two_wheeler_spots() >= self.two_wheeler_spot_limit:
                raise exceptions.ParkingFull(f" Two wheeler parking is full. ")
            Parking.two_wheeler_spots.update({spot._id(): spot})

        elif vehicle.get_type() in [VehicleType.bus, VehicleType.truck]:
            if self._available_truck_spots() >= self.truck_spot_limit:
                raise exceptions.ParkingFull(f" Truck/Bus parking is full. ")
            Parking.truck_spots.update({spot._id(): spot})

    def park_vehicle(self, type: VehicleType):
        try:
            vehicle = VehicleFactory().create(type)
            spot = ParkingSpotFactory().create(type)
            self._assign_spot(vehicle, spot)
            ticket = vehicle.attach_ticket(spot._id())
            Parking.tickets.update({str(ticket.number): ticket})
            return ticket
        except exceptions.ParkingFull as e:
            print(e)
        return None

    def unpark_vehicle(self, type_: str, ticket_number: int):
        parking_receipt = ParkingReceipt()
        issued_ticket = self.parking_ticket(str(ticket_number))
        spot_number = issued_ticket.spot_number
        self.free_spot(type_, spot_number)
        parking_receipt.generate(issued_ticket, Parking.fee_model)
        return parking_receipt