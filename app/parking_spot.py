from abc import ABC, abstractmethod
from app.enumerations import ParkingSpotType
from app.vehicle import Vehicle
import app.config as cfg
from app.enumerations import VehicleType

class ParkingSpot(ABC):

    _SPOT_ID = 0

    def __init__(self) -> None:
        super().__init__()
        self.sid: int
        self.type: ParkingSpotType
        self.occupied: bool = False
        self.vehicle: Vehicle

    @abstractmethod    
    def _id(self):
        pass


class TwoWheelerSpot(ParkingSpot):
    def __init__(self) -> None:
        super().__init__()
        self.set_id()
        self.type = ParkingSpotType.two_wheeler

    def set_id(self):
        ParkingSpot._SPOT_ID += 1
        self.sid = ParkingSpot._SPOT_ID

    def _id(self):
        return self.sid

class CarSpot(ParkingSpot):
    def __init__(self) -> None:
        super().__init__()
        self.set_id()
        self.type = ParkingSpotType.car
    
    def set_id(self):
        ParkingSpot._SPOT_ID += 1
        self.sid = ParkingSpot._SPOT_ID

    def _id(self):
        return self.sid

class BusSpot(ParkingSpot):
    def __init__(self) -> None:
        super().__init__()
        self.set_id()
        self.type = ParkingSpotType.bus

    def set_id(self):
        ParkingSpot._SPOT_ID += 1
        self.sid = ParkingSpot._SPOT_ID

    def _id(self):
        return self.sid

class ParkingSpotFactory:
    def create(self, type: VehicleType):
        if type in [VehicleType.bus, VehicleType.truck]:
            return BusSpot()
        elif type in [VehicleType.car, VehicleType.suv]:
            return CarSpot()
        elif type in [VehicleType.motorcycle, VehicleType.scooter]:
            return TwoWheelerSpot()
