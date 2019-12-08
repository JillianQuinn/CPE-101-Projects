# Name:		Jillian Quinn 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set I
# Term:         Winter 2019

"""
Because this assignment does not use functions, all source code must be indented in the block below. Future assignments - which will make use of functions - will not have this requirement
"""

if __name__ == "__main__":

    
    # Problem I
    x = input("Enter a number between 1 and 20: ")
    StartNum = x    
    x = int(x)
    StartNum = int(StartNum)
    x = x * 2
    x = 10 + x
    x = x / 2
    x = x - StartNum
    print("x = " + str(x))

    
    # Problem II
    x = input("Enter a number: ")
    x = int(x)
    y = input("Enter another number: ")
    y = int(y)
    sum1 = x + y
    sum2 = y + sum1
    sum3 = sum1 + sum2
    sum4 = sum2 + sum3
    sum5 = sum3 + sum4
    sum6 = sum4 + sum5
    sum7 = sum5 + sum6
    sum8 = sum6 + sum7
    ans = (x + y + sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8) / sum5 
    print("Answer = " + str(ans))  


    # Problem III
    x = input("Enter a 4 digit number with different digits: ")
    x = int(x)
    last = x % 10
    first = x // 1000
    second = (x // 100) % 10
    third = (x % 100) // 10
    swapped = (last * 1000) + (second * 100) + (third * 10) + (first)
    smaller = min(x, swapped)   
    larger = max(x, swapped)
    diff = larger - smaller
    diffsum = ((diff % 10) + (diff // 1000) + ((diff // 100) % 10) +
    ((diff % 100) // 10))
    endsum = (diffsum % 10) + (diffsum // 10)
    print(endsum)  


    # Problem IV
    x = input("Enter a number between 1 and 50: ")
    ans = 50 / 7
    dec = (ans % 1) * 1000000
    dec = int(dec)
    first = dec // 100000
    last = dec % 10
    second = (dec // 10000) % 10
    third = (dec // 1000) % 10
    fourth = (dec // 100) % 10
    fifth = (dec % 100) // 10
    sum = first + second + third + fourth + fifth + last
    print(sum)


     




