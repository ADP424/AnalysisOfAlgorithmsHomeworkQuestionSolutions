def print_height_map(heights: list, max_height: int):
    for height in heights:
        print(height, end=" ")

    print()
    i = max_height
    while i > 0:
        for height in heights:
            if height >= i:
                print('# ', end="")
            else:
                print('  ', end="")
        i -= 1
        print()

input() # waste first input
heights = [int(i) for i in input().strip().split(' ')] # create a list of n integers
print(len(heights))

# find the tallest point in the graph
max_index = 0
i = 1
while i < len(heights):
    if heights[i] > heights[max_index]:
        max_index = i
    i += 1

print_height_map(heights, heights[max_index])

# split the heights list into to halves at the max point (excluding the max point from both)
left_heights = heights[:max_index]
right_heights = heights[max_index + 1:]

volumes = [0]

# iterate through the left_heights array from the left, counting the volume
local_max_height = -1
i = 0
while i < len(left_heights):
    if left_heights[i] >= local_max_height:
        local_max_height = left_heights[i]
        if(volumes[len(volumes) - 1] > 0):
            volumes.append(0)
    else:
        volumes[len(volumes) - 1] += local_max_height - left_heights[i]
    i += 1

# iterate through the right_heights array from the right, counting the volume
local_max_height = -1
i = len(right_heights) - 1
while i >= 0:
    if right_heights[i] >= local_max_height:
        local_max_height = right_heights[i]
        if(volumes[len(volumes) - 1] > 0):
            volumes.append(0)
    else:
        volumes[len(volumes) - 1] += local_max_height - right_heights[i]
    i -= 1

print(volumes)
print(max(volumes))