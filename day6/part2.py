import sys

with open(sys.path[0] + '/input.txt') as f:
    school = [int(f) for f in f.readline().split(',')]
# print(school)


# https://www.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/hnyl6fs/
def solve(data, days):
    tracker = [data.count(i) for i in range(9)]
    print(tracker)
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
        print(tracker)
    return sum(tracker)

print(f"Part 2: {solve([0,1,2], 20)}")



# step =7
# day = 7
# while True:
#     newSchool = [f for f in school]
#     day += step
#     step += step
#     [newSchool.append(f + 2) for f in school]
#     if(step > 256/2):
#         break
#     school = [f for f in newSchool]

# print(f"day {day} has {len(school)} fish")


# for i in range(day, 256):
#     newSchool=[]
#     for f in school:
#         if (f == 0):
#             newSchool.append(6)
#             newSchool.append(8)
#         else:
#             newSchool.append(f-1)
#     # print(f"Day {i} has {len(newSchool)} fish")
#     school = [fish for fish in newSchool] #deepcopy
# print(len(school))




# [print(f"n={n}, day={7*n} \t{5*(2**n)}") for n in range (0, 37)]
# print(256/7)
# print(2*(2**(256/7)))

# # 3 4 3 1 2                 day 0
# # 3 4 3 1 2 -> 3 4 5 5 6    day 7
# # 3 4 3 1 2 3 4 5 5 6 -> 3 4 5 5 5  6 6 7 7 8 day 14
# #                        3 4 5 5 6, 5 6 7 7 8
# # +2
# # 3 4 3 1 2
# # 5 6 5 3 4

# # 7, 14, 21, 28, 35, 42, 49, 56, 63, 70,
                                #         140,
                                # 257  264  273    280,

# 0 -> 5
# 7 -> 10
# 14 -> 20
# 21 -> 40
# 28 -> 80
# 35 -> 160
# 42 -> 320
# 49 -> 640
# 56 -> 1280



# 26 984 457 539
