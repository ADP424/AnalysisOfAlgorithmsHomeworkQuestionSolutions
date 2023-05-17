equation = input().split(' ')

# perform all addition operations first
numbers_to_multiply = []
prev_sum = 0
for i in range(len(equation)):
    if equation[i] == '*':
        numbers_to_multiply.append(prev_sum)
        prev_sum = 0
    elif equation[i] != '+':
        prev_sum += int(equation[i])
numbers_to_multiply.append(prev_sum)

# multiply all the sums together
product = 1
for num in numbers_to_multiply:
    product *= num

print(product)