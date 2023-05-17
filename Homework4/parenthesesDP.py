import sys

equation = input().split(' ')
integers = [] # a list of all the integers, positive and negative, in order

# perform all addition operations first
prev_sum = 0
for i in range(len(equation)):
    if equation[i] == '-':
        integers.append(prev_sum)
        prev_sum = 0
    elif equation[i] != '+':
        prev_sum += int(equation[i])
integers.append(prev_sum)

# dp[i][j] is the maximum value from integer i to integer j
dp = [[-sys.maxsize for _ in range(len(integers))] for _ in range(len(integers))]

# the maximum values from integer i to i is just the integer at position i
for i in range(len(integers)):
    dp[i][i] = integers[i]

# iterate over the subproblems
for d in range(1, len(integers)):
    for i in range(len(integers) - d):
        j = i + d
        for k in range(i, j):
            if k == i:
                dp[i][j] = max(dp[i][j], dp[i][k] - dp[k + 1][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i][k] - dp[k + 1][j], dp[i][k] + dp[k + 1][j])

print(dp[0][len(integers) - 1])