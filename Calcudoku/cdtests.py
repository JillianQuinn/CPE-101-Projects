# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Problem Set 5
# Term:         Winter 2019 


import calcudoku

assert calcudoku.transpose([[4, 1, 2, 5, 3], [1, 5, 4, 3, 2], [2, 3, 5, 4, 1], \
    [3, 4, 1, 2, 5], [5, 2, 3, 1, 4]]) == [[4, 1, 2, 3, 5], [1, 5, 3, 4, 2], \
    [2, 4, 5, 1, 3], [5, 3, 4, 2, 1], [3, 2, 1, 5, 4]]
assert calcudoku.transpose([[1, 2], [2, 3]]) == [[1, 2], [2, 3]]
assert calcudoku.transpose([[6, 9], [1, 4]]) == [[6, 1], [9, 4]]

assert calcudoku.validate_rows([[4, 1, 2, 5, 3], [1, 5, 4, 3, 2], \
    [2, 3, 5, 4, 1], [3, 4, 1, 2, 5], [5, 2, 3, 1, 4]])
assert calcudoku.validate_rows([[8, 1], [4, 0]])
assert not calcudoku.validate_rows([[4, 4], [4, 4]])

# test 1
assert calcudoku.validate_cages([[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], \
    [2, 4, 1, 5, 3], [1, 2, 4, 3, 5], [4, 3, 5, 2, 1]], [[9, 0, 5, 6], \
    [7, 1, 2], [10, 3, 8, 13], [14, 4, 9, 14, 19], [3, 7], [8, 10, 11, \
    16], [13, 12, 17, 21, 22], [5, 15, 20], [6, 18, 23, 24]])
# test 2
assert calcudoku.validate_cages([[1, 2, 3, 4, 5], [3, 1, 4, 5, 2], \
    [2, 5, 1, 3, 4], [5, 4, 2, 1, 3], [4, 3, 5, 2, 1]], [[4, 0, 1, 6], \
    [8, 2, 7, 12], [14, 3, 4, 8], [15, 5, 10, 11, 15], \
    [14, 9, 13, 14, 18, 19, 24], [11, 16, 20, 21], [9, 17, 22, 23]])
# Test 3
assert calcudoku.validate_cages([[1, 4, 2, 5, 3], [2, 5, 4, 3, 1], \
    [5, 2, 3, 1, 4], [4, 3, 1, 2, 5], [3, 1, 5, 4, 2]], [[7, 0, 1, 2], \
    [12, 3, 4, 8, 9], [17, 5, 7, 10, 11, 12, 13], [5, 6], [11, 14, 19, 24], \
    [7, 15, 20], [5, 16, 17, 21], [11, 18, 22, 23]])
# cages filled, total value is less than expeted
assert not calcudoku.validate_cages([[1, 2], [3, 4]], [[4, 0, 1], [8, 2, 3]])
# cages not filled, total value is less
assert calcudoku.validate_cages([[1, 0], [3, 0]], [[4, 0, 1], [8, 2, 3]])
# cages filled, total value is greater than expected
assert not calcudoku.validate_cages([[1, 2], [3, 4]], [[2, 0, 1], [8, 2, 3]])
# cages not filled, total value greater than expected
assert not calcudoku.validate_cages([[2, 0], [3, 0]], [[1, 0, 1], [2, 2, 3]])
# cages filled with zeros
assert calcudoku.validate_cages([[0, 0], [0, 0]], [[1, 0, 1], [2, 2, 3]])
# cages filled and correct
assert calcudoku.validate_cages([[2, 1], [3, 4]], [[3, 0, 1], [7, 2, 3]])
# cages not filled, value greater
assert not calcudoku.validate_cages([[2, 0], [3, 0]], [[1, 0, 1], [2, 2, 3]]) 
# cages not filled, value less
assert calcudoku.validate_cages([[2, 0], [3, 0]], [[3, 0, 1], [5, 2, 3]])
# cages zero
assert calcudoku.validate_cages([[0, 0], [0, 0]], [[3, 0, 1], [5, 2, 3]])
# sum of not filled greater than expected
assert not calcudoku.validate_cages([[1, 1], [0, 3]], [[1, 0, 1], [2, 2, 3]])
assert not calcudoku.validate_cages([[1, 3], [3, 0]], [[4, 0, 1], [2, 2, 3]])
assert not calcudoku.validate_cages([[1, 3], [0, 4]], [[4, 0, 1], [2, 2, 3]])

