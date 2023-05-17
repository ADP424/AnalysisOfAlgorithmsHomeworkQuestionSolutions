sum = 0
for i in range(int(input())):
    input_num = int(input())
    if input_num % 2 == 0:
        sum += input_num
print(sum)