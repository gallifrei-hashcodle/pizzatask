# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:41:25 2018

@author: Filip
"""


class Car(object):
    def __init__(self, current_row, current_column, is_busy, car_id, newxt_finish_time):
        self.current_row = current_row
        self.current_column = current_column
        self.is_busy = is_busy
        self.car_id = car_id
        self.newxt_finish_time = newxt_finish_time
        self.assigned_rides = []

    def assign_ride(self, ride, start_time):
        self.assigned_rides.append(ride.ride_id)
        self.current_row = ride.end_row
        self.current_column = ride.end_column
        self.newxt_finish_time = start_time + ride.duration

    def is_busy(self, time):
        return time < self.newxt_finish_time



