# This program asks the user to think of a number between 1 and n. Then asks for a number of groups.
# The program then prints out groups of numbers and asks in which group the correct number is.
# When enough inputs have been given to deduce the correct number, the program will print it.

import random
import math
 
size = int(input("Enter a number:\n"))
numbers = [int(i) for i in range(1,size+1)]
 
random.shuffle(numbers)
input("Think of a number (1-%d). [Hit 'Enter' when done]\n" %size)
base = 0
while True:
    base = int(input("Enter the number of groups to use (>1):\n"))
    if base > 1:
        break
   
num_cycles = math.ceil(math.log(len(numbers),base))
numbers_list = []
 
for cycle in range(num_cycles):
    print("In which group is your number?")
    temp_numbers = []
   
    for b in range(base):
        print("Group %d:\n         " %(b+1), end='')
        for i in range(b,len(numbers),base):
            print(numbers[i], end=' ')
            temp_numbers.append(numbers[i])
        print()
 
    for i in range(int(input("\n"))-1,len(numbers),base):
        numbers_list.append(numbers[i])
   
    numbers = temp_numbers[:]
 
for i in range(len(numbers)//base+1):
    if numbers_list.count(numbers_list[i]) == num_cycles:
        print("Your number is:\n%s" %numbers_list[i])
        break
