input() # waste first input that gives the size of the array
A = [int(i) for i in input().split(' ')] # create a list of distinct integers out of the space-separated input, which we assume is sorted ascending

# high and low are defined as if indexing starting at 1, as in the problem specifications
high = len(A)
low = 1
while True:
    mid = (high + low) // 2

    if mid == A[mid - 1]:
        print("TRUE")
        break

    if high <= low:
        print("FALSE")
        break
    
    # if the middle index is greater than the middle value, it is impossible for the index and value to match in the lower half of the array
    if mid > A[mid - 1]: # -1 because python indexes starting 0, not 1
        low = mid + 1
    # if the middle index is less than the middle value, it is impossible for the index and value to match in the upper half of the array
    elif mid < A[mid - 1]:
        high = mid - 1