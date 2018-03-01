class Ride(object):
    def __init__(self, start_row, start_column, end_row, end_column, start_time, end_time):
        self.start_row = start_row
        self.start_column = start_column
        self.end_row = end_row
        self.end_column = end_column
        self.start_time = start_time
        self.end_time = end_time
        self.duration = abs(start_row - end_row) + abs(start_column - end_column)

    def latest_possible_start_time(self):
        return self.end_time - self.duration