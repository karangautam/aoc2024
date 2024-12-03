"""
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""

import re
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from myutils.read_input import read_problem_input_string


def main():
    problem_input = read_problem_input_string('02/input.txt')
    current_split_string = "don't()"
    sub_problem_input = problem_input.split(current_split_string,1)
    correct_sub_problem_input = ""
    while len(sub_problem_input) > 1:
        if current_split_string == "don't()":
            correct_sub_problem_input += sub_problem_input[0]
            current_split_string = "do()"

        else:

            current_split_string = "don't()"
        sub_problem_input = sub_problem_input[1].split(current_split_string,1)
    print(get_multiplication_sum(correct_sub_problem_input))


def get_multiplication_sum(problem_input):
    return sum([int(i.split('(')[1].split(',')[0]) * int(i.split(',')[1].split(')')[0]) for i in
                re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', problem_input)])


if __name__ == '__main__':
    main()