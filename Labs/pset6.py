# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Problem Set 5
# Term:         Winter 2019


def poly_add(poly1, poly2):
    poly_add = []
    for i in range(3):
        poly_add.append(poly1[i] + poly2[i])
    return poly_add

def poly_mul(poly1, poly2):
    poly_foil = []
    simplified = []
    for i in range(3):
        for j in range(3):
            poly_foil.append(poly1[i] * poly2[j])
    simplified = [poly_foil[0], poly_foil[1] + poly_foil[3], poly_foil[2] + \
         poly_foil[4] + poly_foil[6] , poly_foil[5] + poly_foil[7], poly_foil[8]]
    return simplified


def index_of_smallest(ints):
    if ints == []:
        return -1
    else:
        smallest = ints[0]
        for i in range(len(ints)):
            if smallest > ints[i]:
                smallest = ints[i]
        return ints.index(smallest)

def remove_duplicates(ints):
    no_dups = []
    for i in ints:
        if i not in no_dups:
            no_dups.append(i)
    return no_dups

def products(int_lists):
    product = []
    total = 1
    for i in range(len(int_lists)):    
        if int_lists[i] == []:
           product.append(0)
        else:
            for j in range(len(int_lists[i])):
                total *= int_lists[i][j]
            product.append(total)
            total = 1
    return product


def fibonacci(n):
    a = 0
    b = 1
    fib = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib
    count = 0
    while count < n - 2:
        c = a + b
        fib.append(c)
        a = b
        b = c
        count += 1
    return fib


def geo_mean(numbers):
    product = 1
    if len(numbers) == 0:
        return 0 
    for i in range(len(numbers)):
        product *= numbers[i]
    mean = product ** (1 / len(numbers))
    return mean


def nest_lists(n):
    nested = []
    for i in range(n - 1):
        nested = [nested]
    return nested


def solve_bool_exp(bool_exp, bools):
    if len(bool_exp) == 3:
        if bool_exp[1] == "and":
            return bools[0] and bools[1]
        else: 
            return bools[0] or bools[1]
    if len(bool_exp) == 4:
        if bool_exp[1] == "and":
            return bools[0] and not bools[1]
        elif bool_exp[1] == "or":
            return bools[0] or not bools[1]
        elif bool_exp[2] == "and":
            return not bools[0] and bools[1]
        elif bool_exp[2] == "or":
            return not bools[0] or bools[1]
    if len(bool_exp) == 5:
        if bool_exp[2] == "and":
            return not bools[0] and not bools[1]
        else:
            return not bools[0] or not bools[1]
