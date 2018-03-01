import in_out
import sort



def get_car_with_least_waiting_time(ride):
    pass


def solve():
    data = in_out.read_task('Inputs/a_example.in')
    all_rides = data['ride_list']
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




