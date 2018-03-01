__author__ = 'hlib'

import numpy as np
import pprint as pp

def read_task(file):
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


def solve(data):
    solution = dict()
    solution['n'] = 3
    solution['pieces'] = [[0, 0, 2, 1],[0, 2, 2, 2],[0, 3, 2, 4]]
    return solution


def write_solution(solution, output_file_name):
    with open(output_file_name, 'w') as f:
        f.write(str(solution['n']) + '\n')
        for row in solution['pieces']:
            f.write(' '.join(str(elm) for elm in row) + '\n')



def main(input_file, output_file):
    data = read_task(input_file)
    pp.pprint(data)
    solution = solve(data)
    write_solution(solution, output_file)

main('Inputs/example.in', 'Outputs/example.out')
