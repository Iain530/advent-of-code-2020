# Usage:    part 1: python day_1.py input_file
#           part 2: python day_1.py input_file 3 

from itertools import combinations
import sys


if len(sys.argv) < 2:
    print("Must specify input file")
    exit(1)


with open(sys.argv[1]) as f:
    expense_report = [int(entry) for entry in f.readlines()]


def find_first_sum_combination(expense_report, sum_total, group_size):
    for comb in combinations(expense_report, group_size):
        if sum(comb) == sum_total:
            return comb


def multiply(*args):
    if len(args) < 1:
        return None

    result = 1
    for num in args:
        result *= num
    return result


sum_total = 2020 
group_size = int(sys.argv[2]) if len(sys.argv) > 2 else 2  # Default part 1

result = find_first_sum_combination(expense_report, sum_total, group_size)
if result:
    print(f"Answer: {multiply(*result)}")
else:
    print("No pair matching the target sum")
