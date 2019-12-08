# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Problem Set 4
# Term:         Winter 2019


def mul(x, y):
    i = 0
    product = 0
    while (i < y):
       product = product + x
       i += 1
    return product


def exp(x, y):
    i = 0
    total = 1
    while (i < y):
        total = mul(total, x)
        i += 1
    return total


def div(x, y):
    quotient = 0
    while (y <= x):
        x = x - y
        quotient += 1
    return quotient


def mod(x, y):
    while (x >= y):
        x = x - y
    return x
        

def greatest_factor(x):
    i = 1
    greatest = 1
    while (i <= 9):
        if (x % i) == 0:
            greatest = i
        i += 1
    return greatest


def sum_ints(start, stop, step):
    sum = 0
    while (start < stop):
        sum = sum + start
        start += step
    return sum


def sum_mul_table(max_int):
    i = 1
    sum = 0
    while (i <= max_int):
        sum = sum + sum_ints(i, max_int * i + 1 , i)
        i += 1
    return sum


def all_input():
    u_input = input("Enter an input: ")
    concat = u_input
    while(u_input != ""):
        u_input = input("Enter an input: ")
        concat = concat + u_input
    return concat
