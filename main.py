import in_out

__author__ = 'hlib'

import slice as slices
import pizzacut

def cut_all_pizza(pizza, min_ingredients, max_size):
    rows = len(pizza)
    column = len(pizza[0])
    slice_list = []
    for i in range (rows):
        for j in range (column):
            slice = slices.basic_slice(1, i, j)
            print(i)
            while slice is not None:
                if pizzacut.canCut(pizza, [[slice.up_row, slice.up_column], [slice.down_row, slice.down_column]],
                                   min_ingredients, max_size):
                    pizzacut.pizzaCutting(pizza, [[slice.up_row, slice.up_column], [slice.down_row, slice.down_column]])
                    slice_list.append([slice.up_row, slice.up_column, slice.down_row, slice.down_column])
                    print("piece added " + str(len(slice_list)))
                    break
                else:
                    slice = slices.Slice(slice.up_row, slice.up_column, slice.down_row, slice.down_column).transform(max_size)
    return slice_list


import in_out

data = in_out.read_task('Inputs/example.in')
ps = cut_all_pizza(data['pizza'].tolist(), data['L'], data['H'])
solution = {'pieces': ps, 'n': len(ps)}
in_out.write_solution(solution, 'Outputs/example.out')
