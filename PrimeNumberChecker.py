from math import ceil

print("This program will determine whether an integer is prime or not.")
value = int(input("Enter a integer, 2 or greater, to be tested: ")) # collect user input

if value < 2: # ensuring value is within domain
    print("Invalid test value!")
    value = int(input("Enter a integer, 2 or greater, to be tested: "))

limit = ceil(value/2) # highest factor to test
test_factor = 2 # start with factor of 2

while test_factor <= limit:
    if value%test_factor == 0: # factor found
        break
    else:
        test_factor += 1 # augment factor by 1

if value == 2:
    print("2 is prime!") # special case of value = 2
else:
    if value%test_factor == 0:
        print(str(value) + " is composite. " + str(test_factor) + " is its lowest factor.") # composite return
    else:
        print(str(value) + " is prime!") # prime return