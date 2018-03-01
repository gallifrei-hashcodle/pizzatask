from pprint import pprint
# import  numpy as np
import  ride


def read_task(file):
    data = dict()
    with open(file, 'r') as f:
        line = f.readline()
        split_line = line.split(' ')
        data['rows'] = int(split_line[0])
        data['columns'] = int(split_line[1])
        data['vehicles'] = int(split_line[2])
        data['rides'] = int(split_line[3])
        data['bonus'] = int(split_line[4])
        data['steps'] = int(split_line[5])
        rides = list()
        counter = 0
        for line in f:
            spl = line.split(' ')

            tmp_ride = ride.Ride(int(spl[0]), int(spl[1]), int(spl[2]), int(spl[3]), int(spl[4]), int(spl[5]), counter)
            rides.append(tmp_ride)
            counter += 1
        data['rides_list'] = rides
        return data

def generate_outputFiles(carList):
  file = open("Output/c_no_hurry.out","w")
  for car in carList:
      carDetails = str(len(car.assigned_rides))

      for ride in car.assigned_rides:
          carDetails = carDetails + " "+ str(ride)
      file.write(str(carDetails) + "\n")
  file.close()


# print(read_task("Inputs/a_example.in"))
