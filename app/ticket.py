
from app.enumerations import VehicleType


class ParkingTicket:

    TICKET_NUMBER: int = 0

    def __init__(self):
        self.number: int
        self.spot_number: int
        self.entry_date_time: str
        self.vehicle_type: VehicleType

    def __repr__(self):
        return f'Ticket number: {self.number}\nSpot number: {self.spot_number}\nEntry d&t: {self.entry_date_time}\nVehicle type: {self.vehicle_type}'

    def generate(self, spot, dtime, vehicle_type):
        self.spot_number = spot
        self.entry_date_time = dtime
        self.vehicle_type = vehicle_type
        self._set_ticket_number()

    def _set_ticket_number(self):
        ParkingTicket.TICKET_NUMBER += 1
        self.number = ParkingTicket.TICKET_NUMBER
