# Name:         Jillian Quinn
# Course:       CPE 101
# Instructor:   Kauffman
# Assignment:   Pixel Magic
# Term:         Winter 2019

import sys


def main():
    filter_mode, file_name, run = "", "", True
    try:
        filter_mode, file_name = sys.argv[1], sys.argv[2]
    except:
        print("Usage: python pixelmagic.py <mode> <image>")
        run = False
    if run:
        try:
            fp = open_file(file_name)
            fp.readline()
            width_height, color = fp.readline(), fp.readline()
            lines = fp.readlines()
            fp.close()
            width_height = width_height.strip("\n").split(" ")
            max_color = color.strip("\n")
            for i in range(len(lines)):
                lines[i] = lines[i].strip("\n").split(" ")
                for j in range(len(lines[i])):
                    lines[i][j] = int(lines[i][j])
            width, height = int(width_height[0]) - 1, int(width_height[1])
            if filter_mode == "find":
                decode_pass(lines, width, height, max_color)
            elif filter_mode == "fade":
                fade_pass(lines, width,  max_color, height)
            elif filter_mode == "blur":
                blur_pass(lines, width, max_color, height)
            else:
                print("Error: Invalid Mode")
        except FileNotFoundError or not file_name.endswith(".ppm"):
            print("Error: Unable to Open {0}".format(file_name))


def decode_pass(lines, width, height, max_color):
    pixels = find_image(lines)
    fp = open_file("decoded.ppm")
    fp.write("P3\n{0} {1}\n{2}\n".format(width + 1, height, max_color))
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j] = str(pixels[i][j])
        fp.write(" ".join(pixels[i]))
        fp.write("\n")
    fp.close()


def fade_pass(lines, width, max_color, height):
    row = col = radius = 0
    try:
        row = int(sys.argv[3])
        col = int(sys.argv[4])
        radius = int(sys.argv[5])
        pixels = fade_image(lines, width + 1, row, col, radius)
        fp = open_file("faded.ppm")
        fp.write("P3\n{0} {1}\n{2}\n".format(width + 1, height, max_color))
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                pixels[i][j] = str(pixels[i][j])
            fp.write(" ".join(pixels[i]))
            fp.write("\n")
        fp.close()
    except:
        print("Usage: python pixelmagic.py fade <image> <row> <col> <radius>")


def blur_pass(lines, width, max_color, height):
    if len(sys.argv) < 4:
        reach = 4
    else:
        reach = int(sys.argv[3])
    pixels = blur_image(lines, width + 1, reach)
    fp = open_file("blurred.ppm")
    fp.write("P3\n{0} {1}\n{2}\n".format(width + 1, height, max_color))
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j] = str(pixels[i][j])
        fp.write(" ".join(pixels[i]))
        fp.write("\n")
    fp.close()


def open_file(file_name):
    if file_name == "puzzle.ppm":
        return open("puzzle.ppm", "r")
    if file_name == "mouse.ppm":
        return open("mouse.ppm", "r")
    if file_name == "lights.ppm":
        return open("lights.ppm", "r")
    if file_name == "decoded.ppm":
        return open("decoded.ppm", "w")
    if file_name == "faded.ppm":
        return open("faded.ppm", "w")
    if file_name == "blurred.ppm":
        return open("blurred.ppm", "w")
    raise FileNotFoundError


def find_image(pixels):
    for i in range(len(pixels)):
        red = pixels[i][0]
        red *= 10
        if red > 255:
            red = 255
        pixels[i][0] = red
        pixels[i][1] = red
        pixels[i][2] = red
    return pixels


def fade_image(pixels, width, row, col, radius):
    for i in range(len(pixels)):
        temp_row = i // width
        temp_col = i % width
        distance = ((temp_row - row) ** 2 + (temp_col - col) ** 2) ** 0.5
        scale = ((radius - distance) / radius)
        if scale < 0.2:
            scale = 0.2
        pixels[i][0] = int(pixels[i][0] * scale)
        pixels[i][1] = int(pixels[i][1] * scale)
        pixels[i][2] = int(pixels[i][2] * scale)
    return pixels


def blur_image(pixels, width, reach):
    total_rows = (len(pixels) - 1) // width
    total_cols = (len(pixels) - 1) % width
    new_pixels = []
    for i in range(len(pixels)):
        row, col = i // width, i % width
        r_sum = g_sum = b_sum = 0
        total_width = (reach * 2) + 1
        top_left_row, top_left_col = row - reach, col - reach
        bottom_right_row, bottom_right_col = row + reach, col + reach
        if top_left_col < 0:
            total_width, top_left_col = top_left_col + total_width, 0
        if bottom_right_col > total_cols:
            total_width, bottom_right_col = total_cols - col + 1 + reach, \
                total_cols
        colors = calc_blur(total_rows, top_left_row, bottom_right_row, width, \
            top_left_col, total_width, pixels, r_sum, g_sum, b_sum)
        new_pixels.append([colors[0], colors[1], colors[2]])
    return new_pixels


def calc_blur(total_rows, top_left_row, bottom_right_row, width, top_left_col, \
    total_width, pixels, r_sum, g_sum, b_sum):
    count, colors = 0, []
    if top_left_row < 0:
            top_left_row = 0
    if bottom_right_row > total_rows:
            bottom_right_row = total_rows
    if total_width > width:
        total_width = width
    while top_left_row <= bottom_right_row:
        index = top_left_row * width + top_left_col
        for j in range(total_width):
            if (index + j) < len(pixels):
                count += 1
                r_sum += pixels[index + j][0]
                g_sum += pixels[index + j][1]
                b_sum += pixels[index + j][2]
        top_left_row += 1
    if count > 0:
        colors = [int(r_sum / count), int(g_sum / count), int(b_sum / count)]
    return colors


if __name__ == "__main__":
    main()



