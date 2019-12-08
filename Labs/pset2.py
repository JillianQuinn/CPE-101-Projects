# Name:         Jillian Quinn 
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set 2
# Term:         Winter 2019


def print_hello(name):
    print("Hello " + name)    


def get_numbers():
    num = input("Enter an integer: ")
    num2 = input("Enter another integer: ")
    num = int(num)
    num2 = int(num2)
    return num + num2


def cube(integer):
    return integer ** 3


def get_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5


def find_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def find_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    side1 = find_distance(x1, y1, x2, y2)
    side2 = find_distance(x2, y2, x3, y3)
    side3 = find_distance(x1, y1, x3, y3)
    return side1 + side2 + side3


def do_math(x, y):
    return (3 * (x ** 2) + 4 * y) / (2 * x)


