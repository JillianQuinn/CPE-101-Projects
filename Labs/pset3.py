# Name:         Jillian Quinn
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set 3
# Term:         Winter 2019


def is_positive(x):
    return x > 0


def both_positive(x, y):
    return is_positive(x) and is_positive(y)


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def is_isosceles_triangle(a, b, c):
    return (is_triangle(a, b, c)) and (a == b or a == c or c == b)


def max_of_two(a, b):
    if a >= b:
        return a
    else:
        return b


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
   
 
def mix_colors(a, b):
    if a == b:
        return a
    elif (a == "red" or a == "yellow") and (b == "red" or b == "yellow"):
        return "orange"
    elif (a == "yellow" or a == "blue") and (b == "yellow" or b == "blue"):
        return "green"
    else:
        return "purple" 


def find_discriminant(a, b, c):
    disc =  b ** 2 - 4 * a * c
    if disc < 0:
        return None
    else:
        return disc


def solve_poly(a, b, c):
    if find_discriminant(a, b, c) == None:
        return None
    else:
       return (-b + find_discriminant(a, b, c)  ** 0.5) / (2 * a)
