from pprint import pprint
import  numpy as np

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


def write_solution(solution, output_file_name):
    with open(output_file_name, 'w') as f:
        f.write(str(solution['n']) + '\n')
        for row in solution['pieces']:
            f.write(' '.join(str(elm) for elm in row) + '\n')


def read_solution(output_file_name):
    data = dict()
    pieces = []
    with open(output_file_name, 'r') as f:
        n_pieces = int(f.readline())
        for i in range(0, n_pieces):
            piece = [list(map(int, f.readline().split(' ')))]
            pieces.append(piece)
    data['pieces'] = pieces
    return data

