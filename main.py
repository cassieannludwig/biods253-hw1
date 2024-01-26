# Run Pascal's Triangle with 10 lines

import matplotlib.pyplot as plt
import time

def pascal_triangle(num_lines):
    pascal_list = [[1], [1, 1]]
    prev_line = [1, 1]
    for i in range(num_lines-2):
        this_line = pairwise_sum(prev_line)
        pascal_list.append(this_line)
        prev_line = this_line

    print_pascal(pascal_list)


def pairwise_sum(prev_line):
    new_line = [1] * (len(prev_line) + 1)
    for i in range(len(prev_line) - 1):
        new_line[i+1] = prev_line[i] + prev_line[i+1]

    return new_line


def print_pascal(given_list):
    print('\n'.join([str(l).strip('[]') for l in given_list]))

def plot_pascal(num_lines, time_taken):
    """ Graph where the x axis is the number of lines printed
    and the y axis is the time taken to generate a triangle with that many lines"""

    plt.plot(num_lines, time_taken)
    plt.xlabel('Number of lines')
    plt.ylabel('Time taken (seconds)')
    plt.title('Pascal\'s Triangle')
    plt.show()

if __name__ == '__main__':
    pascal_triangle(15)

    times = []
    lines = range(1, 16)
    for num_lines in lines:
        start_time = time.time()
        pascal_triangle(num_lines)
        end_time = time.time()
        times.append(end_time - start_time)

    plot_pascal(list(lines), times)

