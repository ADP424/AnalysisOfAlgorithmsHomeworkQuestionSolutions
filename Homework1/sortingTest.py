from math import sqrt
import random
import time
import numpy as np

# creates a list of list_size random floats with Gaussian distribution and tests each sort on them
def test_sorts_gaussian(list_size: int):
    list1 = []
    for _ in range(list_size):
        list1.append(random.gauss(0.5, 1/10000))
    list2 = list1.copy() # makes two copies of the list so the list isn't already sorted
    list3 = list1.copy() # avoids the sorting algorithms having to waste time copying the list

    start_time = time.time()
    merge_sort(list1)
    end_time = time.time()
    print("Merge sort took", round(end_time - start_time, 5), " seconds to run for", list_size, "elements")

    start_time = time.time()
    insertion_sort(list2)
    end_time = time.time()
    print("Insertion sort took", round(end_time - start_time, 5), " seconds to run for", list_size, "elements")

    start_time = time.time()
    bucket_sort(list3, int(sqrt(list_size))) # use sqrt(list_size) buckets so there's the same number of elements per bucket on average
    end_time = time.time()
    print("Bucket sort took", round(end_time - start_time, 5), " seconds to run for", list_size, "elements")

# creates a list of list_size random floats with uniform distribution and tests each sort on them
def test_sorts_uniform(list_size: int):
    list1 = np.random.uniform(-1, 1, list_size)
    list2 = list1.copy() # makes two copies of the list so the list isn't already sorted
    list3 = list1.copy() # avoids the sorting algorithms having to waste time copying the list

    start_time = time.time()
    merge_sort(list1)
    end_time = time.time()
    print("Merge sort took", round(end_time - start_time, 5), " seconds to run for", list_size, "elements")

    start_time = time.time()
    insertion_sort(list2)
    end_time = time.time()
    print("Insertion sort took", round(end_time - start_time, 5), " seconds to run for", list_size, "elements")

    start_time = time.time()
    bucket_sort(list3, int(sqrt(list_size))) # use sqrt(list_size) buckets so there's the same number of elements per bucket on average
    end_time = time.time()
    print("Bucket sort took", round(end_time - start_time, 5), " seconds to run for", list_size, "elements")

# splits the list up recursively into lists of size 1, then merges the lists together in pairs in order
def merge_sort(list: list):
    new_list = list
    if(len(list) <= 1): # if the list is size 1, return and let the merging happen
        return new_list

    midpoint = len(new_list) // 2
    left_list = merge_sort(new_list[:midpoint])
    right_list = merge_sort(new_list[midpoint:])

    return merge(left_list, right_list) # merge the lists together after they're each sorted and return

# helper function for merge_sort that merges the two lists together
def merge(left_list: list, right_list: list):
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

# iterates over the array and swaps two adjacent elements if the left element is greater than the right element
def insertion_sort(list: list):
    for index in range(1, len(list)):
        temp = list[index]
        position = index

        while position > 0 and list[position - 1] > temp:
            list[position] = list[position - 1]
            position = position - 1

        list[position] = temp
    
    return list

# splits the list into num_buckets even buckets
def bucket_sort(list: list, num_buckets: int):
    # finds the min and max values in list
    min = 100000
    max = -100000
    for element in list:
        if max < element:
            max = element
        elif min > element:
            min = element
    
    # creates an interval based on the range of the values and num_buckets
    interval = (max - min) / num_buckets
    
    # creates a list of intervals to be used for inserting elements into buckets later
    intervals = []
    for i in range(num_buckets):
        intervals.append((i + 1) * interval + min)
    intervals[num_buckets - 1] += 1 # adds 1 to the final interval to counteract float rounding, making the max value bigger than the max interval

    # creates a list of num_buckets empty lists
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])

    # sorts the elements into their respective buckets
    for element in list:
        # go through the list of intervals until the element fits in one of the ranges
        bucket_index = 0
        for interval in intervals:
            if element <= interval:
                break
            bucket_index += 1
            
        buckets[bucket_index].append(element)

    # sorts each bucket using insertion sort and combines them into one big array
    new_list = []
    for bucket in buckets:
        new_list += insertion_sort(bucket)

    return new_list

print("Sort tests with Gaussian distribution:")
test_sorts_gaussian(100)
test_sorts_gaussian(1000)
test_sorts_gaussian(10000)
test_sorts_gaussian(100000)

print("\nSort tests with uniform distribution:")
test_sorts_uniform(100)
test_sorts_uniform(1000)
test_sorts_uniform(10000)
test_sorts_uniform(100000)