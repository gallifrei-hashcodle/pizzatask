import sys
import in_out
import car
import sort


def initialiseCars(data):
    numberOfCars = data['vehicles']
    carList = []
    for x in range(0, numberOfCars):
        carList.append(car.Car(0,0,False,x,0))
    return carList

data = in_out.read_task('Inputs/b_should_be_easy.in')
carList = initialiseCars(data)

def distance_to_car(start_row, start_column, current_row, current_column):
    return abs(start_row - current_row) + abs(start_column - current_column)


def get_car_with_least_waiting_time(ride, current_time):
    least_waiting_time = sys.maxsize
    car_with_least_waiting_time = None
    distance_to_car1 = None
    for car in [car for car in carList if car.is_busy1(current_time) == False]:
        distance_to_car1 = distance_to_car(ride.start_row, ride.start_column, car.current_row, car.current_column)
        time = ride.start_time - (current_time + distance_to_car1)
        if time < least_waiting_time:
            least_waiting_time = time
            car_with_least_waiting_time = car
    return car_with_least_waiting_time, distance_to_car1


def in_time_for_ride(ride, current_time, time_to_car):
    return current_time+time_to_car+ride.duration <= ride.end_time

def solve():
    all_rides = data['rides_list']
    sort.sortRidesByStartTime(all_rides)
    total_time = data['steps']
    current_time = 0
    pending_rides = all_rides
    assigned_rides = []
    while current_time < total_time and len(pending_rides) > 0:
        for ride in all_rides:
            if ride in pending_rides:
                assigned_car, time_to_car = get_car_with_least_waiting_time(ride, current_time)
                if assigned_car is None:
                    continue
                else:
                    pending_rides.remove(ride)
                    if in_time_for_ride(ride, current_time, time_to_car):
                        assigned_car.assign_ride(ride, current_time + time_to_car)
                        assigned_rides.append(ride)
        current_time += 1

    for car in carList:
        print (str(car.car_id) + " " + str(car.assigned_rides))

solve()



