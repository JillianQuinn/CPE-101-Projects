# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Calcudoku
# Term:         Winter 2019 


def main():
    num_cages = input()
    num_cages = int(num_cages)
    cages = []
    for i in range(num_cages):
        cages.append([int(num) for num in input().split(" ")])
    grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, \
         0], [0, 0, 0, 0, 0]]
    i = 0
    while i < 25:
        column = i % 5
        row = i // 5
        grid[row][column] += 1
        if (grid[row][column] > 5):
            grid[row][column] = 0
            i -= 1
        else:
            if (validate_rows(grid) and validate_rows(transpose(grid)) and \
                validate_cages(grid, cages)):
                i += 1
    for i in range(len(grid)):
        strs = [str(i) for i in grid[i]]
        print(" ".join(strs))


def transpose(grid):
    transposed = []
    inner = []
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            inner.append(grid[j][i])
        transposed.append(inner)
        inner = []
    return transposed


def validate_rows(grid):
    check = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i].count(grid[i][j]) > 1 and grid[i][j] != 0:
                check = False
    return check


def validate_cages(grid, cages):
    sum_cage = 0
    zero = False
    for i in range(len(cages)):
        for j in range(1, len(cages[i])):
            row = cages[i][j] // len(grid)
            column = cages[i][j] % len(grid)
            if grid[row][column] == 0:
                zero = True
            if sum_cage >= cages[i][0]:
                return False
            sum_cage += grid[row][column]
        if zero and sum_cage >= cages[i][0]:
            return False
        elif not zero and sum_cage != cages[i][0]:
            return False
        else:
            sum_cage = 0
            zero = False
    return True


if __name__ == "__main__":
    main()
