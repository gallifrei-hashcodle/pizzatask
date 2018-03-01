import in_out
data = in_out.read_task('Inputs/a_example.in')
all_rides = data['rides_list']

def sortRidesByStartTime(all_rides):

    for ride1 in range(len(all_rides)-1):
        for ride2 in range(1,len(all_rides)):
            if(all_rides[ride1].start_time > all_rides[ride2].start_time):
                print(str(all_rides[ride1].start_time) + " " + str( all_rides[ride2].start_time))
                temp = all_rides[ride1]
                all_rides[ride1] = all_rides[ride2];
                all_rides[ride2] = temp;
    return  all_rides
print("here"+ str(sortRidesByStartTime(all_rides)))