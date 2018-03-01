import in_out

class Slice:
    def __init__(self, coordinates):
        self.r1 = coordinates[0]
        self.r2 = coordinates[2]
        self.c1 = coordinates[1]
        self.c2 = coordinates[3]
    def __str__(self):
        return  "r1: {0} r2: {1} c1: {2} c2: {3}".format(self.r1, self.r2, self.c1, self.c2)
    def __repr__(self):
        return '( '+str(self)+ ' )'

def check_overlap(sl1, sl2):

    if sl1.r1 < sl2.r2 and sl1.r2 > sl2.r1  and sl1.c1 < sl2.c2 and sl1.c2 > sl2.c1:
        return  True
    return  False

def check_if_any_overlaps(slices):

    for i in range(0, len(slices)):

        for j in range(i+1, len(slices)):

            if i<len(slices) and j < len(slices) and i!=j:

                res = check_overlap(slices[i],slices[j])
                if res:
                    return True
    return  False

def is_more_than_max_size(slice, H):
    if (slice.r2-slice.r1+1) * (slice.c2-slice.c1+1) >H:
        return True
    return  False
def check_if_insufficient_ingredients(slice, pizza, L):
    #print(slice)
    t_count=0
    m_count=0
    for i in range(slice.r1, slice.r2+1):
        for j in range(slice.c1, slice.c2+1):
            if int(pizza[i][j])==1:
                t_count+=1
            else:
                m_count+=1
    if(t_count<L or m_count<L):
        return True
    #print('slice done')
    return False
def calculate_score(slices):
    sum = 0
    for slice in slices:
        sum +=(slice.r2-slice.r1+1) * (slice.c2-slice.c1+1)
    return  sum

def validate(input_file, output_file):
    pizza = in_out.read_task(input_file)
    print(pizza['pizza'])
    slices = list()
    slice_nr = 0
    with open(output_file, 'r') as f:
        slice_nr = int(f.readline())
        for line in f:
            x = tuple([int(i) for i in line.split(' ')])
            slices.append(Slice(x))

        #print(slices)
    if(check_if_any_overlaps(slices)):
        print("Error: Slices Overlap")
        return
    for sl in slices:
        if is_more_than_max_size(sl,pizza['H']):
            print("Error: Max Size error")
            return
        if(check_if_insufficient_ingredients(sl,pizza['pizza'], pizza['L'])):
            print("Not enough Mushrooms or Tomatoes")
            return
    print("Your Score Is {0}".format(calculate_score(slices)))
validate('Inputs/big.in', 'Outputs/big.out')
