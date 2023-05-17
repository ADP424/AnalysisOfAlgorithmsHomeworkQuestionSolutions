stringX = input() # size n
stringY = input() # size m

# create a dynamic programming array with n + 1 rows and m + 1 columns
dp = [[0 for _ in range(len(stringY) + 1)] for _ in range(len(stringX) + 1)]

for i in range(len(stringX) + 1):
    for j in range(len(stringY) + 1):
        if i == 0: # if there's no letters in string X, the minimum cost is inserting every letter from string Y
            dp[i][j] = j * 4
        elif j == 0: # if there's no letters in string Y, the minimum cost is removing every letter from string X
            dp[i][j] = i * 3
        elif stringX[i - 1] == stringY[j - 1]: # if the letters are the same, no change has to be made
            dp[i][j] = dp[i - 1][j - 1]
        else:
            del_cost = dp[i - 1][j] + 3 # the cost of deleting a character

            ins_cost = dp[i][j - 1] + 4 # the cost of inserting a character

            rep_cost = dp[i - 2][j - 1] + 5 # the cost of replacing two consecutive characters with one character
            
            if i >= 2: # if there aren't two previous characters, replacing two consecutive characters isn't a valid operation
                dp[i][j] = min(del_cost, ins_cost, rep_cost)
            else:
                dp[i][j] = min(del_cost, ins_cost)

print(dp[len(stringX)][len(stringY)])