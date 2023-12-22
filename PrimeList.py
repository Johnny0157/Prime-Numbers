from math import ceil
# list of primes generator

low = int(input("Enter lowest test integer (at least 2): ")) # seek lower end of test list
while low < 2:
    low = int(input("Enter lowest test integer (at least 2): "))

high = int(input("Enter highest test integer (greater than lowest): ")) # seek higher end of test list
while low >= high:
    high = int(input("Enter highest test integer (greater than lowest): "))

primes_list = []
potential_prime = low

while potential_prime <= high:
    test_factor = 2
    limit = ceil(potential_prime/2)
    if potential_prime == 2:
        isPrime = True
    else:
        while test_factor <= limit:
            if potential_prime % test_factor == 0:
                isPrime = False
                break
            else:
                test_factor += 1
                if test_factor == limit + 1:
                    isPrime = True
                    break
    if isPrime == True:
        primes_list.append(potential_prime)
    potential_prime += 1

print(primes_list)