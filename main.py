inputstart = int(input('Enter the beginning of the interval: '))
inputend = int(input('Enter the end of the interval: '))

for i in range(inputstart, inputend):  # Iterating over numbers from a given interval
    
    firstnum = 0  # The sum of the divisors of the second number = The first number of the pair
    secnum = 0  # The sum of the divisors of the first number = the second number of the pair

    # We are looking for divisors of the first number of the pair
    for x in range(1, i):
        if i % x == 0:      # We are looking for divisors
            secnum += x     # And sum the divisors

    # We are looking for divisors of the second number of the pair
    for y in range(1, secnum):
        if secnum % y == 0:     # We are looking for divisors
            firstnum += y       # And sum the divisors

    # We check whether the found numbers satisfy the condition that:
    #           - the first number of the pair is the sum of the divisors of the second number of the pair
    #           - the first number of the pair is not the second number of the pair
    #           - the first number of the pair is the minimum in this pair
    if (i == firstnum) & (i != secnum) & (i == min(i, secnum)):
        print(firstnum, secnum)
