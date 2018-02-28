__author__ = 'hlib'

import numpy as np
import pprint as pp

def read_input(file):
    data = dict()
    with open(file, 'r') as f:
        line = f.readline()
        split_line = line.split(' ')
        data['rows'] = int(split_line[0])
        data['columns'] = int(split_line[1])
        data['L'] = int(split_line[2])
        data['H'] = int(split_line[3])
        matrix = np.zeros(shape=(data['rows'],data['columns']))
        for i in range(data['rows']):
            line = f.readline()
            for j in range(len(line)):
                if line[j] == 'T':
                    matrix[i][j] = 1

        data['pizza'] = matrix
        return data


def main(file):
    data = read_input(file)
    pp.pprint(data)

main('Inputs/example.in')
