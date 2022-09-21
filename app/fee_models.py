from abc import ABC, abstractmethod

from app.enumerations import VehicleType
from app.ticket import ParkingTicket
from app.utils import Utils

util = Utils()


class FeeModel(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.fee_structure: dict = {}

    @abstractmethod
    def estimated_fees(self, ticket):
        pass

class MallFeeModel(FeeModel):
    def __init__(self) -> None:
        super().__init__()
        self.fee_structure = {
            'two_wheeler': 10,
            'four_wheeler': 20,
            'trucks': 50
        }

    def estimated_fees(self, ticket: ParkingTicket):
        if ticket.vehicle_type in [VehicleType.motorcycle, VehicleType.scooter]:
            return self.fee_structure.get('two_wheeler', 0)
        elif ticket.vehicle_type in [VehicleType.car, VehicleType.suv]:
            return self.fee_structure.get('four_wheeler', 0)
        elif ticket.vehicle_type in [VehicleType.bus, VehicleType.truck]:
            return self.fee_structure.get('trucks', 0)

class StadiumFeeModel(FeeModel):
    def __init__(self) -> None:
        super().__init__()
        self.fee_structure = {
            'two_wheeler': {
                '0-4': 30,
                '4-12': 60,
                'per_hour': 100
            },
            'four_wheeler': {
                '0-4': 60,
                '4-12': 120,
                'per_hour': 200
            },
            'trucks': None
        }
    
    def _two_wheeler_parking_fee(self, hours=0, minutes=0):
        fees = 0
        if hours > 11:
                fees = self.fee_structure.get('two_wheeler').get('per_hour') * (hours - 11)
                if minutes > 0:
                    fees += self.fee_structure.get('two_wheeler').get('per_hour')
                hours = 11
        if hours in range(4, 12):
                fees += self.fee_structure.get('two_wheeler').get('4-12')
                hours = 3
        if hours in range(0, 4):
                fees += self.fee_structure.get('two_wheeler').get('0-4')
        return fees

    def _four_wheeler_parking_fee(self, hours=0, minutes=0):
        fees = 0
        if hours > 11:
                fees = self.fee_structure.get('four_wheeler').get('per_hour') * (hours - 11)
                if minutes > 0:
                    fees += self.fee_structure.get('four_wheeler').get('per_hour')
                hours = 11
        if hours in range(4, 12):
                fees += self.fee_structure.get('four_wheeler').get('4-12')
                hours = 3
        if hours in range(0, 4):
                fees += self.fee_structure.get('four_wheeler').get('0-4')
        return fees

    def _truck_parking_fee(self, hours=0, minutes=0):
        return 0

    def _total_parking_time(self, ticket: ParkingTicket):
        parking_time = ticket.entry_date_time
        parked_for = util.current_time() - parking_time
        _, hours_spent, minutes_spent = util.time_breakup(parked_for)
        return hours_spent, minutes_spent

    def estimated_fees(self, ticket: ParkingTicket):
        
        fees = 0
        hours_spent, minutes_spent = self._total_parking_time(ticket)

        if ticket.vehicle_type in [VehicleType.motorcycle, VehicleType.scooter]:
            fees = self._two_wheeler_parking_fee(hours_spent, minutes_spent)

        elif ticket.vehicle_type in [VehicleType.car, VehicleType.suv]:
            fees = self._four_wheeler_parking_fee(hours_spent, minutes_spent)

        elif ticket.vehicle_type in [VehicleType.truck, VehicleType.bus]:
            fees = self._truck_parking_fee(hours_spent, minutes_spent)
        return fees

class AirportFeeModel(FeeModel):
    def __init__(self) -> None:
        super().__init__()
        self.fee_structure = {
            'two_wheeler': {
                '0-1': 0,
                '1-8': 40,
                '8-24': 60,
                'per_day': 80
            },
            'four_wheeler': {
                '0-12': 60,
                '12-24': 80,
                'per_day': 100
            },
            'trucks': None
        }
    def _two_wheeler_parking_fee(self, days=0, hours=0, minutes=0):
        fees = 0
        if days > 0:
            fees = self.fee_structure.get('two_wheeler').get('per_day') * days
            if hours>0:
                fees += self.fee_structure.get('two_wheeler').get('per_day')
            return fees

        if hours in range(8, 24):
            fees = self.fee_structure.get('two_wheeler').get('8-24')
            if minutes > 0:
                fees += self.fee_structure.get('two_wheeler').get('8-24')
            return fees
                
        if hours in range(1, 8):
            fees += self.fee_structure.get('two_wheeler').get('1-8')
            if minutes > 0:
                fees += self.fee_structure.get('two_wheeler').get('1-8')
            return fees

        if hours in range(0, 1):
            fees += self.fee_structure.get('two_wheeler').get('0-1')
            return fees
        return fees

    def _four_wheeler_parking_fee(self, days = 0, hours=0, minutes=0):
        fees = 0
        if days > 0:
            fees = self.fee_structure.get('four_wheeler').get('per_day') * days
            if hours>0:
                fees += self.fee_structure.get('two_wheeler').get('per_day')
            return fees

        if hours in range(12, 24):
            fees = self.fee_structure.get('four_wheeler').get('12-24')
            if minutes > 0:
                fees += self.fee_structure.get('four_wheeler').get('12-24')
            return fees
                
        if hours in range(0, 12):
            fees += self.fee_structure.get('four_wheeler').get('0-12')
            if minutes > 0:
                fees += self.fee_structure.get('four_wheeler').get('0-12')
            return fees
        return fees

    def _truck_parking_fee(self, hours=0, minutes=0):
        return 0

    def _total_parking_time(self, ticket: ParkingTicket):
        parking_time = ticket.entry_date_time
        parked_for = util.current_time() - parking_time
        days, hours_spent, minutes_spent = util.time_breakup(parked_for)
        return hours_spent, minutes_spent

    def estimated_fees(self, ticket: ParkingTicket):
        
        fees = 0
        hours_spent, minutes_spent = self._total_parking_time(ticket)

        if ticket.vehicle_type in [VehicleType.motorcycle, VehicleType.scooter]:
            fees = self._two_wheeler_parking_fee(hours_spent, minutes_spent)

        elif ticket.vehicle_type in [VehicleType.car, VehicleType.suv]:
            fees = self._four_wheeler_parking_fee(hours_spent, minutes_spent)

        elif ticket.vehicle_type in [VehicleType.truck, VehicleType.bus]:
            fees = self._truck_parking_fee(hours_spent, minutes_spent)
        return fees


