class Ride(object):
    def __init__(self, start_row, start_column, end_row, end_column, start_time, end_time, ride_id):
        self.start_row = start_row
        self.start_column = start_column
        self.end_row = end_row
        self.end_column = end_column
        self.start_time = start_time
        self.end_time = end_time
        self.duration = abs(start_row - end_row) + abs(start_column - end_column)
        self.ride_id = ride_id

    def latest_possible_start_time(self):
        return self.end_time - self.duration

    def __str__(self):
        return "id: {0}, start_row: {1}, start_col: {2}, start_time: {3}".format(self.ride_id,self.start_row, self.start_column, self.start_time)
    def __repr__(self):
        return '( '+str(self)+' )'