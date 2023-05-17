input() # waste the first input specifying the input size
X = [int(i) for i in input().split(' ')]

dp = [1] * len(X) # dynamic programming array for finding the longest subsequence
counts = [1] * len(X) # dynamic programming array for holding the count of longest subsequences so far

for i in range(1, len(X)): # count the sequence up until each number
    for j in range(i):
        if X[j] < X[i]: # if the left-most number is smaller than the right-most
            if dp[j] + 1 > dp[i]: # if this subsequence is longer than the last one, change the count and subsequence length
                dp[i] = dp[j] + 1
                counts[i] = counts[j]
            elif dp[j] + 1 == dp[i]: # if this subsquence is the same as the longest, increase the count of that length of subsequence
                counts[i] += counts[j]

longest_subsequence = max(dp)
total_count = 0
for i in range(len(dp)):
    if dp[i] == longest_subsequence:
        total_count += counts[i]

print(total_count)