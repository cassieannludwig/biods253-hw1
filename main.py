# Run Pascal's Triangle with 10 lines

import time
import matplotlib.pyplot as plt
import sys

def pascal_triangle(num_lines, print_lines = True):
    pascal_list = [[1], [1, 1]]
    prev_line = [1, 1]
    for i in range(num_lines-1):
        this_line = pairwise_sum(prev_line)
        pascal_list.append(this_line)

        prev_line = this_line

    if print_lines:
        print_pascal(pascal_list)


def pairwise_sum(prev_line):
    new_line = [1] * (len(prev_line) + 1)
    for i in range(len(prev_line) - 1):
        new_line[i+1] = prev_line[i] + prev_line[i+1]

    return new_line


def print_pascal(given_list):
    print('\n'.join([str(l).strip('[]') for l in given_list]))
    
def plot_runtime(num_reps = 10):
    
    lines, times = [],[]
    
    for n in range(1,7):
        num_lines = int(10**(n/2))
        
        start_time = time.time()
        for rep in range(num_reps):
            pascal_triangle(num_lines, print_lines = False)
            
        elapsed = (time.time() - start_time)/num_reps
        
        lines.append(num_lines)
        times.append(elapsed)
        
    plt.plot(lines, times)
    plt.yscale('log')
    plt.xscale('log')
    plt.title("Time to run Pascal's Triangle")
    plt.xlabel('Number of lines')
    plt.ylabel('Time (sec)')

    plt.savefig("timing_plot.png")


if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        num_lines = sys.argv[1]
    else:
        num_lines = 15
        
    pascal_triangle(num_lines, print_lines = True)
        
    plot_runtime(num_reps = 10)
    

