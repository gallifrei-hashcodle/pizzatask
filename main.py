import in_out
import car
import sort

def initialiseCars(data):
    numberOfCars = data['vehicles']
    carList = []
    for x in range(0, numberOfCars):
        carList.append(car.Car(0,0,False,x,0))
    return carList


def get_car_with_least_waiting_time(ride):
    pass


def solve():
    data = in_out.read_task('Inputs/a_example.in')
    carList = initialiseCars(data)
    all_rides = data['rides_list']
    sort.sortRidesByStartTime(all_rides)
    total_time = data['steps']
    current_time = 0
    pending_rides = all_rides
    while current_time < total_time and len(pending_rides) > 0:
        for ride in all_rides:
            if ride in pending_rides:
                assigned_car = get_car_with_least_waiting_time(ride)
                assigned_car.assignRide(ride)
                pending_rides.remove(ride)



