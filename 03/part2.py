"""
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from myutils.read_input import read_problem_input

def list_strictly_increasing(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]:
            return False
    return True

def list_strictly_decreasing(lst):
    for i in range(1, len(lst)):
        if lst[i] >= lst[i-1]:
            return False
    return True

def difference_between_adjacent(lst):
    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i-1]) > 3:
            return False
    return True

def main():
    problem_input = read_problem_input('03/input.txt')
    safe_reports = 0
    for i in problem_input:
        input_list = i.split(' ')
        input_list = [int(i) for i in input_list]
        if (list_strictly_increasing(input_list) or list_strictly_decreasing(input_list)) and difference_between_adjacent(input_list):
            safe_reports += 1
        else:
            for j in range(len(input_list)):
                if (list_strictly_increasing(input_list[:j] + input_list[j+1:]) or list_strictly_decreasing(input_list[:j] + input_list[j+1:])) and difference_between_adjacent(input_list[:j] + input_list[j+1:]):
                    safe_reports += 1
                    break
    print(safe_reports)

if __name__ == '__main__':
    main()