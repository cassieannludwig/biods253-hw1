# Run Pascal's Triangle with 10 lines

def pascal_triangle(num_lines):
    pascal_list = [[1], [1, 1]]
    prev_line = [1, 1]
    for i in range(num_lines-1):
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


if __name__ == '__main__':
    pascal_triangle(10)

