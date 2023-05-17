"""
Authors: Aidan Dalgarno-Platt
         Liam Coleman
"""

# We're basically counting the number of inversions with the added wrench of the -1s having different rules

# NOTE: I borrowed this merge_sort from my answer for the previous homework
# I adjusted the comparison in merge so that it sorts in descending rather than ascending order
# I also changed it so that merge_sort and merge take "left" and "right" fields
# This lets merge keep track of each element's place in the whole list
# We need this because the number of elements for each inversion depends on its size compared to all the elements after it
# Merge sort of course takes O(nlog(n)) time to complete
num_inversions = 0
def merge_sort(list: list, left: int, right: int):
    new_list = list
    if(len(list) <= 1): # if the list is size 1, return and let the merging happen
        return new_list

    midpoint = (len(new_list) - 1) // 2
    left_list = merge_sort(new_list[:midpoint + 1], left, (left + right) // 2)
    right_list = merge_sort(new_list[midpoint + 1:], (left + right) // 2 + 1, right)

    return merge(left_list, right_list, left, right) # merge the lists together after they're each sorted and return

# helper function for merge_sort that merges the two lists together
def merge(left_list: list, right_list: list, left: int, right):
    new_list = []

    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        # go up the left and right lists, adding each element to new_list in order of size
        # if arr[i] >= arr[j], there's no need for an inversion (i.e [4, 2])
        if(left_list[i] >= right_list[j]):
            new_list.append(left_list[i])
            i += 1
        else:
            new_list.append(right_list[j])
            j += 1
            global num_inversions
            num_inversions += ((left + right) // 2 - (left + i) + 1)

    # add any left over elements to new_list from whichever list had the biggest values
    while(i < len(left_list)):
        new_list.append(left_list[i])
        i += 1
    while(j < len(right_list)):
        new_list.append(right_list[j])
        j += 1

    return new_list

input() # waste first input that gives the size of the list
bullies = [int(i) for i in input().strip().split(' ')] # create a list of n integers

# Before doing merge sort, split the array by -1s
# We call merge sort on each sub-array between -1, as someone without a lunch will never be bullied
# This takes O(n) time
subbullies = [[]]
for i in range(len(bullies)):
    if bullies[i] == -1:
        if len(subbullies[len(subbullies) - 1]) == 0:
            continue
        subbullies.append([])
        continue
    subbullies[len(subbullies) - 1].append(bullies[i])

# Each merge_sort takes O(mlog(m)) time where m is num elements in each subbully
# Let's say there are k subbullies
# All the m's add up to n - k elements
# In any case, the total runtime of this section is still O(nlog(n)) because it's several O(mlog(m)) where m < n added together
for subbully in subbullies:
    merge_sort(subbully, 0, len(subbully) - 1)
print(num_inversions)