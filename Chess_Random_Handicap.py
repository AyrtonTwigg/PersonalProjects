import random

material_num = int(input("How many material points? (1-39)\n"))

material_values =     [9,5,3,1]
max_material_values = [1,2,4,8]
material_solutions =  []

def find_solutions(curr_list, highest_num):
    list_sum = sum(curr_list)
    if list_sum > material_num:
        return
    elif list_sum == material_num:
        material_solutions.append(curr_list)
    
    for x in material_values:
        if x <= highest_num:
            list_copy = curr_list.copy()
            list_copy.append(x)
            find_solutions(list_copy, x)

find_solutions([],material_values[0])

temp = material_solutions.copy()
for solution in temp:
    for i in range(len(material_values)):
        count = solution.count(material_values[i])
        if count > max_material_values[i]:
            material_solutions.remove(solution)
            break

random_solution = random.choice(material_solutions)

queen =  0
rook =   0
bishop = 0
knight = 0
pawn =   0
for element in random_solution:
    if element == 1:
        pawn += 1
    elif element == 3:
        if bishop == 2:
            knight += 1
        elif knight == 2:
            bishop += 1
        elif random.random() < 0.5:
            bishop += 1
        else:
            knight += 1
    elif element == 5:
        rook += 1
    elif element == 9:
        queen += 1

if queen:
    print("The Queen")

if rook == 2:
    print("Both rooks")
elif rook == 1:
    if random.random() < 0.5:
        print("The a-rook")
    else:
        print("The h-rook")

if bishop == 2:
    print("Both bishops")
elif bishop == 1:
    if random.random() < 0.5:
        print("The c-bishop")
    else:
        print("The f-bishop")

if knight == 2:
    print("Both knights")
elif knight == 1:
    if random.random() < 0.5:
        print("The b-knight")
    else:
        print("The g-knight")

if pawn > 0:
    file_choices = ["a", "b", "c", "d", "e", "f", "g", "h"]
    while len(file_choices) > pawn:
        file_choices.pop(random.randrange(len(file_choices)))

    print("The ", end='')
    comma = False
    for file in file_choices:
        if comma:
            print(",", end='')
        else:
            comma = True
        print(file, end='')
    
    if pawn == 1:
        print("-pawn")
    else:
        print("-pawns")
