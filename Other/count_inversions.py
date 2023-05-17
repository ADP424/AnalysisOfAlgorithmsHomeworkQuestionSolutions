num_inversions = 0
weighted_inversions = 0

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
        if(left_list[i] < right_list[j]):
            new_list.append(left_list[i])
            i += 1
        else:
            new_list.append(right_list[j])
            j += 1
            global num_inversions
            num_inversions += ((left + right) // 2 - (left + i) + 1)
            
            global weighted_inversions
            k = right // 2 - i
            while k >= (left + i):
                print(i, k)
                weighted_inversions += left_list[i] + right_list[k]
                k -= 1

    # add any left over elements to new_list from whichever list had the biggest values
    while(i < len(left_list)):
        new_list.append(left_list[i])
        i += 1
    while(j < len(right_list)):
        new_list.append(right_list[j])
        j += 1

    return new_list

list = [7, 3, 8, 1, 5]
merge_sort(list, 0, len(list) - 1)
print(num_inversions)
print(weighted_inversions)