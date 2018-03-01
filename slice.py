def basic_slice(size, start_row, start_column):
    return Slice(start_row, start_column, start_row, start_column + size)

class Slice(object):
    def __init__(self, up_row, up_column, down_row, down_column):
        self.up_row = up_row
        self.up_column = up_column
        self.down_row = down_row
        self.down_column = down_column

    def size(self):
        return self.rows() * self.columns()

    def rows(self):
        return self.down_row - self.up_row + 1

    def columns(self):
        return self.down_column - self.up_column + 1

    def transform(self, max_size):
        size = self.size()
        if self.rows() / self.columns() == size and self.rows() % self.columns() == 0:
            if size < max_size:
                return basic_slice(++size, self.up_row, self.up_column)
            else:
                return None
        else:
            new_rows = self.rows() + 1
            while size % new_rows != 0 and new_rows < size:
                new_rows += 1
            new_columns = size / new_rows
            return Slice(self.up_row, self.up_column, self.up_row + new_rows - 1, self.up_column + new_columns - 1)

    def __str__(self):
        return str([self.up_row, self.up_column, self.down_row, self.down_column])


