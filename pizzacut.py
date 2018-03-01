
pizza = [[0,0,0,1],[1,1,0,0]]
#slice coordinates
slice = [[0,0],[0,1]]


def pizzaCutting(pizza, slice):
   for item in range(slice[0][0], slice[1][0]+1):
       for item2 in range(slice[0][1], slice[1][1]+1):
             pizza[item][item2] = -1
   return pizza

def canCut(pizza, slice, minNoIngredient, maxCells):
    countTomato = 0
    countMushroom = 0
    countCells = 0
    for item in range(slice[0][0], slice[1][0] + 1):
        for item2 in range(slice[0][1], slice[1][1] + 1):
            try:
                countCells +=1
                if(pizza[item][item2] == -1):
                    return False
                else:
                     if  pizza[item][item2] == 0:
                        countTomato += 1
                     if pizza[item][item2] == 1:
                        countMushroom += 1
            except IndexError:
                return False

    if countTomato >= minNoIngredient and countMushroom >= minNoIngredient and countCells <= maxCells:
        return True
    else:
        return False


