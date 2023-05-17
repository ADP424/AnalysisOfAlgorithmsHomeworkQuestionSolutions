"""
Authors: Aidan Dalgarno-Platt
         Liam Coleman
"""

# NOTE: I took this merge sort from my previous Homework 1 submission (again)
# The runtime is O(nlog(n)) obviously
def merge_sort(list: list):
    new_list = list
    if(len(list) <= 1): # if the list is size 1, return and let the merging happen
        return new_list

    midpoint = len(new_list) // 2
    left_list = merge_sort(new_list[:midpoint])
    right_list = merge_sort(new_list[midpoint:])

    return merge(left_list, right_list) # merge the lists together after they're each sorted and return

# helper function for merge_sort that merges the two lists together
# this part of merge sort is O(n)
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

def run_kitchen():
    num_foods = int(input()) # the total number of foods, delivered or not
    foods_dict = dict() # dictionary containing all foods (key = delivery time unit, value = list of expiration dates)
    max_expiration = 0 # the latest expiration time unit in the whole list
    delivery_dates = [] # list of all time_units that have a delivery on them (list of all keys in foods_dict)

    # create a dictionary with delivery times as the key and lists of food expirations as the values
    # food expirations have the delivery times added on
    # also records the max expiration value in the list
    # this takes O(n) time
    curr_delivery_time = -1
    for _ in range(num_foods):
        food = [int(i) for i in input().split(' ')]
        if curr_delivery_time != food[0]:
            curr_delivery_time = food[0]
            foods_dict[curr_delivery_time] = []
            delivery_dates.append(curr_delivery_time)
        foods_dict[curr_delivery_time].append(food[1] + food[0])

        if (food[1] + food[0]) > max_expiration:
            max_expiration = food[1] + food[0]

    # sort each list in the dictionary using merge sort
    # overall, this takes O(nlog(n)) time
    for key in foods_dict.keys():
        foods_dict[key] = merge_sort(foods_dict[key])

    curr_time_unit = 0
    delivered_food = []
    num_deliveries = 0
    while curr_time_unit <= max_expiration:
        # if there's food arriving this time unit, add it to the pile (in order)
        if curr_time_unit in foods_dict:
            delivered_food = merge(delivered_food, foods_dict[curr_time_unit]) # O(n) time
            num_deliveries += 1

        # if the length of delivered_food is zero, skip until the next delivery
        if len(delivered_food) == 0:
            # if delivered_food is empty and there's no more deliveries left, success!
            if (num_deliveries + 1) >= len(delivery_dates):
                print("YES")
                return
            curr_time_unit = delivery_dates[num_deliveries]
            continue

        # if the food is already expired, the chef has failed and it is impossible
        if (delivered_food.pop(0) - curr_time_unit) <= 0:  # pop is O(1) when called on the first index
            print("NO")
            return

        curr_time_unit += 1

    print("YES")

run_kitchen()