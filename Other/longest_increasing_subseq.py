def longest_increasing_subseq(arr):
    OPT = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        OPT[i] = 1
        for j in range(i):
            if arr[j] < arr[i] and OPT[i] <= OPT[j]:
                OPT[i] = OPT[j] + 1
    return max(OPT)

arr = [2, 4, 7, 1, 5]
print(longest_increasing_subseq(arr))