"""
Author: Aidan Dalgarno-Platt
"""

# NOTE: I took this merge sort from my previous Homework 1 submission (again)
# The runtime is O(nlog(n)) obviously
import time


def merge_sort_normal(list: list):
    new_list = list
    if(len(list) <= 1): # if the list is size 1, return and let the merging happen
        return new_list

    midpoint = len(new_list) // 2
    left_list = merge_sort_normal(new_list[:midpoint])
    right_list = merge_sort_normal(new_list[midpoint:])

    return merge_normal(left_list, right_list) # merge the lists together after they're each sorted and return

# helper function for merge_sort_normal that merges the two lists together
# this part of merge sort is O(n)
def merge_normal(left_list: list, right_list: list):
    new_list = []

    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        # go up the left and right lists, adding them to new_list in order of size
        if(left_list[i] < right_list[j]):
            new_list.append(left_list[i])
            i += 1
        else:
            new_list.append(right_list[j])
            j += 1

    # add any left over elements to new_list from whichever list had the biggest values
    while(i < len(left_list)):
        new_list.append(left_list[i])
        i += 1
    while(j < len(right_list)):
        new_list.append(right_list[j])
        j += 1

    return new_list

# Adjusted merge_sort that indexes correctly to sort the outer list in the format I used for this problem
# The runtime is still O(nlog(n))
def merge_sort_x_coordinates(list: list):
    new_list = list
    if(len(list) <= 1): # if the list is size 1, return and let the merging happen
        return new_list

    midpoint = len(new_list) // 2
    left_list = merge_sort_x_coordinates(new_list[:midpoint])
    right_list = merge_sort_x_coordinates(new_list[midpoint:])

    return merge_x_coordinates(left_list, right_list) # merge the lists together after they're each sorted and return

# helper function for merge_sort_x_coordinates that merges the two lists together
# this part of merge sort is O(n)
def merge_x_coordinates(left_list: list, right_list: list):
    new_list = []

    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        # go up the left and right lists, adding them to new_list in order of size
        if(left_list[i][0] < right_list[j][0]):
            new_list.append(left_list[i])
            i += 1
        else:
            new_list.append(right_list[j])
            j += 1

    # add any left over elements to new_list from whichever list had the biggest values
    while(i < len(left_list)):
        new_list.append(left_list[i])
        i += 1
    while(j < len(right_list)):
        new_list.append(right_list[j])
        j += 1

    return new_list

# binary search implementation that first searches by x-coordinate and then y-coordinate
# still takes overall O(log(n)), since it's searching through n coordinates, just split up in a weird way
# worst case #1, every x-coordinate has only 1 y in its list
# takes O(log(n)) to find the right x-coordinate, then O(1) to find the right y-coordinate, so total O(log(n))
# worst case #2, every y-coordinate is paired up with the same x-coordinate
# takes O(1) to find the right x-coordinate and then O(log(n)) to find the right y-coordinate, so total O(log(n))
# the worst case for this scenario is still O(log(n))
def binary_search(list, coordinate_pair) -> bool:
    high = len(list) - 1
    low = 0
    while True:
        x_mid = (high + low) // 2

        if coordinate_pair[0] == list[x_mid][0]:
            # once the correct x-coordinate is found, search through the y-coordinates
            high = len(list[x_mid][1]) - 1
            low = 0
            while True:
                y_mid = (high + low) // 2

                if coordinate_pair[1] == list[x_mid][1][y_mid]:
                    return True

                if high <= low: # this means the y-coordinate doesn't exist in the list
                    break

                if coordinate_pair[1] > list[x_mid][1][y_mid]:
                    low = y_mid + 1

                elif coordinate_pair[1] < list[x_mid][1][y_mid]:
                    high = y_mid - 1

        if high <= low: # this means the x-coordinate doesn't exist in the list
            return False

        if coordinate_pair[0] > list[x_mid][0]:
            low = x_mid + 1

        elif coordinate_pair[0] < list[x_mid][0]:
            high = x_mid - 1

num_points = int(input())

points = [] # list of every point on the graph, organized in lists in the form of [x, [y values corresponding to that x]]

# create a list of tuples with x-coordinates and their associated y-coordinates
# this takes O(n) time
curr_x_coordinate = -1
for _ in range(num_points):
    point = [int(i) for i in input().split(' ')]
    if curr_x_coordinate != point[0]:
        curr_x_coordinate = point[0]
        points.append([curr_x_coordinate, []])
    points[len(points) - 1][1].append(point[1])

# sort each list using merge sort
# the total number of elements across every list adds up to n
# in terms of big-O, merge-sorting each sublist is the same as merge-sorting the whole list
# therefore, overall, this takes O(nlog(n)) time
for i in range(len(points)):
    points[i][1] = merge_sort_normal(points[i][1])

# sort the greater list by x_coordinate using an adjusted merge sort
# takes O(nlog(n)) time
points = merge_sort_x_coordinates(points)

# the goal is to find a triple of evenly-spaced colinear points
# if three points are evenly-spaced, then the midpoint of the furthest-apart points is the middle point of the triple
# find the midpoint of every pair of points and then use binary search to check if it's in the list of points
# if the midpoint is in the list of points, there is a triple of evenly-spaced colinear points

triple_exists = False
# the outer loop runs for every x-coordinate
# minus the midpoint checking, this runs in O(n^2) time, as each pair of loops runs over n coordinate pairs together

i = 0
while(i < len(points)): # iterates through the x-coordinates
    j = 0
    while(j < len(points[i][1])): # iterates through the y-coordinates
        k = 0
        while(k < len(points)): # iterates through the x-coordinates
            l = 0
            while(l < len(points[k][1])): # iterates through the y-coordinates
                # avoid checking a point against itself
                if i == k and j == l:
                    break

                # calculate the midpoint
                midpoint = ( (points[i][0] + points[k][0]) / 2, (points[i][1][j] + points[k][1][l]) / 2 )

                # check if the midpoint is a point in the points list
                # Takes O(log(n)) time
                if(binary_search(points, midpoint)):
                    triple_exists = True
                    break

                l += 1
            k += 1
        j += 1
    i += 1

if triple_exists:
    print("YES")
else:
    print("NO")