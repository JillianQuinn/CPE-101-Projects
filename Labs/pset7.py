# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Problem Set 7
# Term:         Winter 2019

# Map

def square_all(ints):
    return [i ** 2 for i in ints]


def add_n_all(ints, n):
    return [i + n for i in ints]


def is_even_all(ints):
    return [i % 2 == 0 for i in ints]


# Filter


def are_positive(ints):
    return [i for i in ints if i > 0]


def are_greater_than_n(ints, n):
    return [i for i in ints if i > n]


def are_divisible_by_n(ints, n):
    return [i for i in ints if n != 0 and i % n == 0]


# Other 


def group(ints, size):
    return [[ints[j] for j in range(i, i + size) if j < len(ints)] for i in \
        range(0, len(ints), size)]


def finals_only(outer):
    return [outer[i][j] for i in range(len(outer)) for j in \
        range(len(outer[i]) - 1, len(outer[i])) if len(outer[i]) > 0]


def multi_list(ints):
    return [[i] * i for i in ints]


def running_total(ints):
   return [sum(ints[i] for i in range(j)) for j in range(1, len(ints) + 1)]


def reverse_lists(outer):
    return [[outer[j][i] for i in range(len(outer[j]) - 1, -1, -1)] for j in \
        range(len(outer) - 1, -1, -1)] 


def column_sum(int_lists):
   return [sum(int_lists[i][j] for i in range(len(int_lists))) for j in \
       range(len(int_lists[0]))] 



