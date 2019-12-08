# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Word Search
# Term:         Winter 2019


def main():
    puzzle = input()
    puzzle = puzzle.strip()
    words = input()
    words = words.strip()
    x = 1
    box = ""
    for i in puzzle:
        box = box + i
        if (x % 10 == 0):
             box = box + "\n"
        x += 1
    print(box)
    total_space = words.count(" ") + 1
    index = 0
    while (index < total_space):
        word = parse_word(words, index)
        print(find_word(puzzle, word))
        index += 1


def parse_word(words, index):
    string = ""
    count = 0
    for i in range(0, len(words)):
        if (count == index and words[i] != " "):
            string += words[i]
        if words[i] == " ":
            count += 1
    return string


def find_word(puzzle, word):
    orig_word = word
    if (word in puzzle):
        direction = "(FORWARD)"
    elif (reverse_string(word) in puzzle):
        word = reverse_string(word)
        direction = "(BACKWARD)"
    elif (word in transpose_string(puzzle, 10)):
        puzzle = transpose_string(puzzle, 10)
        direction = "(DOWN)"
    elif (reverse_string(word) in transpose_string(puzzle, 10)):
        puzzle = transpose_string(puzzle, 10)
        word = reverse_string(word)
        direction = "(UP)"
    else:
        return word + ": " + "word not found"
    row = find_row(puzzle, word, direction)
    column = find_column(puzzle, word, direction)
    return (orig_word + ": " + direction + " row: " + str(row) + " column: " + (
        str(column)))


def find_row(puzzle, word, direction):
    if direction == "(FORWARD)":
        row = puzzle.find(word) // 10 
    elif direction == "(BACKWARD)":
        row = (puzzle.find(word) + len(word) - 1) // 10
    elif direction == "(UP)":
        row = puzzle.find(word) % 10 + len(word) - 1
    else:
        row = puzzle.find(word) % 10
    return row


def find_column(puzzle, word, direction):
    if direction == "(FORWARD)":
        column = puzzle.find(word) % 10
    elif direction == "(BACKWARD)":
        column = puzzle.find(word) % 10  + len(word) - 1
    elif direction == "(UP)":
        column = (puzzle.find(word) + len(word) - 1) // 10
    else:
        column = puzzle.find(word) // 10
    return column


def reverse_string(string):
    i = len(string) - 1
    reverse = ""
    while i >= 0:
        reverse = reverse + string[i]
        i -= 1
    return reverse


def transpose_string(string, row_len):
    transposed = ""
    j = 0
    while(j < row_len):
        for i in range(j, len(string), row_len):
            transposed = transposed + string[i]
        j += 1
    return transposed


if __name__ == "__main__":
    main()
