import unittest
from app.enumerations import VehicleType
from app.parking import Parking
from app.fee_models import MallFeeModel, AirportFeeModel, StadiumFeeModel
from app.parking_spot import TwoWheelerSpot
from app.receipt import ParkingReceipt
from app.ticket import ParkingTicket
from app.utils import Utils


class TestParking(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_park_vehicle(self):
        strategy = MallFeeModel()
        two_wheeler_spots = 2
        four_wheeler_spots = 5
        truck_spots = 3
        parking = Parking(strategy, two_wheeler_spots, four_wheeler_spots, truck_spots)
        parking_ticket = parking.park_vehicle(VehicleType.car)
        self.assertEqual(type(parking_ticket), ParkingTicket)

    def test_unpark_vehicle(self):
        strategy = AirportFeeModel()
        two_wheeler_spots = 2
        four_wheeler_spots = 5
        parking = Parking(strategy, two_wheeler_spots, four_wheeler_spots)
        parking_ticket = parking.park_vehicle(VehicleType.car)
        receipt = parking.unpark_vehicle('car', parking_ticket.number)
        self.assertEqual(type(receipt), ParkingReceipt)

    def test_fees(self):
        two_wheeler_spots = 20
        four_wheeler_spots = 50
        stadium = Parking(StadiumFeeModel(), two_wheeler_spots, four_wheeler_spots)
        stadium_parking_ticket = stadium.park_vehicle(VehicleType.scooter)
        receipt1 = stadium.unpark_vehicle('scooter', stadium_parking_ticket.number)


        airport = Parking(AirportFeeModel(), two_wheeler_spots, four_wheeler_spots)
        airport_parking_ticket = airport.park_vehicle(VehicleType.car)
        receipt2 = airport.unpark_vehicle('suv', airport_parking_ticket.number)


        self.assertEqual(receipt1.fees, 30)
        self.assertEqual(receipt2.fees, 60)




if __name__ == '__main__':
    unittest.main()