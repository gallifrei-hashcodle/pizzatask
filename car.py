# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:41:25 2018

@author: Filip
"""


class Car(object):
    def __init__(self, current_row, current_column, is_busy, car_id, next_finish_time):
        self.current_row = current_row
        self.current_column = current_column
        self.is_busy = is_busy
        self.car_id = car_id
        self.next_finish_time = next_finish_time
        self.assigned_rides = []
    
    def __call__(self):
        return (self)

    def assign_ride(self, ride, start_time):
        self.assigned_rides.append(ride.ride_id)
        self.current_row = ride.end_row
        self.current_column = ride.end_column
        self.next_finish_time = start_time + ride.duration

    def is_busy1(self, time):
        return time < self.next_finish_time



