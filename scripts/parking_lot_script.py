import os
import time
from app.enumerations import VehicleType
from app.parking import Parking
from app.fee_models import MallFeeModel, AirportFeeModel, StadiumFeeModel

def to_vehicleType(type_: str) -> VehicleType:
    '''
        For a given string vehicle type it returns the corresponding VehicleType.
    '''
    if type_ in ['motorcycle', 'motorcycles']:
        return VehicleType.motorcycle
    elif type_ in ['scooter', 'scooters']:
        return VehicleType.scooter
    elif type_ in ['car', 'cars']:
        return VehicleType.car
    elif type_ in ['suv', 'suvs']:
        return VehicleType.suv
    elif type_ in ['truck', 'trucks']:
        return VehicleType.truck
    elif type_ in ['bus', 'buses']:
        return VehicleType.bus

def simplify(type_: str) -> str:
    '''
        This method tries to simplify the vehicle types by mapping the plurals to a single string.
    '''
    if type_ in ['motorcycle', 'motorcycles', 'scooter', 'scooters']:
        return 'motorcycle'
    elif type_ in ['car', 'cars', 'suv', 'suvs']:
        return 'car'
    elif type_ in ['truck', 'trucks', 'bus', 'buses']:
        return 'truck'

if __name__ == "__main__":
    output_filename = 'output.txt'

    input1 = 'scripts/example1.txt'
    input2 = 'scripts/example2.txt'
    input3 = 'scripts/example3.txt'

    output = 'scripts/output.txt'

    output_file_path = os.path.join(os.getcwd(), output_filename)
    commands = []


    with open(os.path.join(os.getcwd(), input3), 'r') as fp:  # todo: Change the filename here.
        commands = [item.strip() for item in fp.readlines()]
    
    output_file_fp = open(os.path.join(os.getcwd(), output), 'a')

    two_wheeler_spots = 0
    four_wheeler_spots = 0
    truck_spots = 0
    strategy = None
    parking = None

    for command in commands:
        items = command.split()

        # Set the parking spot counts for different vehicles
        if items[0] == 'spots':
            vehicles = items[1].split('/')
            for vehicle in vehicles:
                if vehicle in ['motorcycle', 'scooter', 'motorcycles', 'scooters']:
                    if items[2].lower() != 'na':
                        two_wheeler_spots += int(items[2])
                elif vehicle in ['suv', 'suvs', 'car', 'cars']:
                    if items[2].lower() != 'na':
                        four_wheeler_spots += int(items[2])
                elif vehicle in ['truck', 'trucks', 'bus', 'buses']:
                    if items[2].lower() != 'na':
                        truck_spots += int(items[2])
        
        # Set the fees strategy for parking
        if items[0] == 'model':
            temp = items[1]
            if temp.lower() == 'mall':
                strategy = MallFeeModel()
            elif temp.lower() == 'airport':
                strategy = AirportFeeModel()
            elif temp.lower() == 'stadium':
                strategy = StadiumFeeModel()
            parking = Parking(strategy, two_wheeler_spots, four_wheeler_spots, truck_spots)
            print(str(parking))

        # Execute the actions
        if items[0] == 'action':
            action = items[1]
            vehicle = items[2]
            if action == 'park':
                vehicleType = to_vehicleType(vehicle)
                ticket = parking.park_vehicle(vehicleType)
                output_file_fp.write(str(ticket) + '\n\n')
            elif action == 'unpark':
                ticket_number = items[3]
                vehicleType = simplify(vehicleType)
                receipt = parking.unpark_vehicle(vehicleType, ticket_number)
                output_file_fp.write(str(receipt) + '\n\n')
    
    output_file_fp.close()
