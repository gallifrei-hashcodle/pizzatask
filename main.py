import in_ou

__author__ = 'hlib'

import pprint as pp


def solve(data):
    solution = dict()
    solution['n'] = 3
    solution['pieces'] = [[0, 0, 2, 1],[0, 2, 2, 2],[0, 3, 2, 4]]
    return solution


def main(input_file, output_file):
    data = in_ou.read_task(input_file)
    pp.pprint(data)
    solution = solve(data)
    in_ou.write_solution(solution, output_file)

main('Inputs/example.in', 'Outputs/example.out')
