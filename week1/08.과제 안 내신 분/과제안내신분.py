import sys

input = sys.stdin.readline

submit_list = [int(input().strip()) for _ in range(28)]
total_list =  [i for i in range(1, 31, 1)]

not_submit_list = []

for idx in total_list:
    if idx not in submit_list:
        not_submit_list.append(idx)

sorted_not_submit_list = sorted(not_submit_list)

for st in sorted_not_submit_list:
    print(st, end="\n")