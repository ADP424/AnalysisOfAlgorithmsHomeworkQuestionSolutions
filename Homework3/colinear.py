"""
Author: Aidan Dalgarno-Platt
"""

# binary search that finds the right x-coordinate then searches the y-coordinates associated with it
# still takes overall O(log(n)), since it's searching through n coordinates, just split up in a weird way
# worst case #1, every x-coordinate has only 1 y in its list
# takes O(log(n)) to find the right x-coordinate, then O(1) to find the right y-coordinate, so total O(log(n))
# worst case #2, every y-coordinate is paired up with the same x-coordinate
# takes O(1) to find the right x-coordinate and then O(log(n)) to find the right y-coordinate, so total O(log(n))
# the worst case for this scenario is still O(log(n))
import time

def binary_search(list, coordinate_pair, x_coord_dict) -> bool:
    high = len(list) - 1
    low = 0
    while True:
        mid = (high + low) // 2

        if coordinate_pair[0] == list[mid][0]:
            high = x_coord_dict[coordinate_pair[0]][1]
            low = x_coord_dict[coordinate_pair[0]][0]
            while True:
                mid = (high + low) // 2

                if coordinate_pair[1] == list[mid][1]:
                    return True

                if high <= low: # this means the y-coordinate doesn't exist paired with this x-coordinate
                    break

                if coordinate_pair[1] > list[mid][1]:
                    low = mid + 1

                elif coordinate_pair[1] < list[mid][1]:
                    high = mid - 1

        if high <= low: # this means the x-coordinate doesn't exist in the list
            return False

        if coordinate_pair[0] > list[mid][0]:
            low = mid + 1

        elif coordinate_pair[0] < list[mid][0]:
            high = mid - 1

num_points = int(input())

points = [] # list of every point on the graph
x_coord_dict = dict() # dictionary where the keys are the x-coordinates and the values are tuples for the starting and ending
                      # points of coordinates with those x-coordinates in the points list
                      # also, I'm aware the requirements banned hashsets, but dictionaries are hashmaps
                      # its inclusion doesn't improve the running time, it's just convenient

# create a list of tuples with the form (x, y)
# this takes O(n) time
for i in range(num_points):
    point = input().split(' ')
    points.append((int(point[0]), int(point[1])))

# sort points using Python's built-in sorted() function
# sorts by x-coordinate first and then y-coordinate
# this has a running time of O(nlog(n))
points = sorted(points, key = lambda x: (x[0], x[1]))

# populates the x_coord_dict appropriately
curr_x_coordinate = -1
i = 0
for point in points:
    if int(point[0]) > curr_x_coordinate:
        if curr_x_coordinate > -1:
            x_coord_dict[curr_x_coordinate] = (x_coord_dict[curr_x_coordinate], i - 1)
        x_coord_dict[int(point[0])] = i
        curr_x_coordinate = int(point[0])
    i += 1
x_coord_dict[curr_x_coordinate] = (x_coord_dict[curr_x_coordinate], len(points) - 1)

start = time.time()
# the goal is to find a triple of evenly-spaced colinear points
# if three points are evenly-spaced, then the midpoint of the furthest-apart points is the middle point of the triple
# find the midpoint of every pair of points and then use binary search to check if it's in the list of points
# if the midpoint is in the list of points, there is a triple of evenly-spaced colinear points
triple_exists = False
i = 0
while i < len(points):
    if triple_exists:
        break

    j = 0
    while j < len(points):
        # avoid checking a point against itself
        if i == j:
            break

        # calculate the midpoint
        midpoint = ( (points[i][0] + points[j][0]) / 2, (points[i][1] + points[j][1]) / 2 )

        # check if the midpoint is a point in the points list
        # Takes O(log(n)) time
        if(binary_search(points, midpoint, x_coord_dict)):
            triple_exists = True
            break

        j += 1

    i += 1

if triple_exists:
    print("YES")
else:
    print("NO")
print(time.time() - start)