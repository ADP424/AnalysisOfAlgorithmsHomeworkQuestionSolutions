import sys

def print_2d_array(array: list):
    for row in array:
        for element in row:
            print(element, end='\t')
        print()
    print()

def counting_rows_and_columns():
    rows = int(input())
    columns = int(input())

    for i in range(rows * columns):
        print(1 + (i // columns) + (i % columns) * rows, end=" ")
        if (i + 1) % columns == 0:
            print()

def draw_out_intervals():
    intervals = []
    for i in range(1, 11):
        intervals.append((2*i - 1, 2*i + 2))

    for interval in intervals:
        for i in range(interval[0]):
            print("  ", end="")
        for i in range(interval[0], interval[1]):
            print("[]", end="")
        print()

# intervals are formatted (time, deadline)
def minimize_lateness(intervals):
    intervals.sort(key = lambda interval : interval[1])
    print(intervals)

    assigned = []
    t = 0
    for i in range (len(intervals)):
        assigned.append((t, t + intervals[i][0]))
        t += intervals[i][0]

    return assigned

# basically works out how many combinations of 2 and 5 dollar bills you can use to form the given number
def midterm_study_guide_problem_five(n: int):
    if n % 2 == 1:
        n -= 5
    return n // 10 + 1

# input is the dimensions of the array (so 5x4, 4x7, 7x2 would be [5, 4, 7, 2])
def matrix_chain_multiplication_min_operations(a: list):
    n = len(a) - 1
    S = [[0 for _ in range(n)] for _ in range(n)]
    
    for d in range(1, n + 1):
        for L in range(1, n - d + 1):
            R = L + d
            S[L - 1][R - 1] = sys.maxsize
            for k in range(L, R):
                tmp = S[L - 1][k - 1] + S[k][R - 1] + a[L - 1] * a[k] * a[R]
                if S[L - 1][R - 1] > tmp:
                    S[L - 1][R - 1] = tmp
    
    # Define helper function to recursively find optimal solution
    def find_optimal_parenthesization(L, R):
        if L == R:
            return f'A{L}'
        else:
            optimal = sys.maxsize
            for k in range(L, R):
                left_expr = find_optimal_parenthesization(L, k)
                right_expr = find_optimal_parenthesization(k+1, R)
                tmp = f'({left_expr} * {right_expr})'
                if S[L - 1][R - 1] == S[L - 1][k - 1] + S[k][R - 1] + a[L - 1] * a[k] * a[R]:
                    optimal = tmp
                    break
            return optimal
    
    # Call helper function on entire range of matrices
    optimal_parenthesization = find_optimal_parenthesization(1, n)
    
    return S[0][n - 1], optimal_parenthesization

# returns a list of every max parenthesization of an equation with + and - signs
# equation formatted like this "1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1"
def find_max_parenthesized_expression(equation):
    def parenthesize(expression):
        n = len(expression)
        if n == 1:
            return [(expression[0], int(expression[0]))]

        result = []
        for i in range(1, n, 2):
            left = expression[:i]
            right = expression[i+1:]
            left_parentheses = parenthesize(left)
            right_parentheses = parenthesize(right)
            for lp in left_parentheses:
                for rp in right_parentheses:
                    if expression[i] == "+":
                        result.append((f"({lp[0]} + {rp[0]})", lp[1]+rp[1]))
                    elif expression[i] == "-":
                        result.append((f"({lp[0]} - {rp[0]})", lp[1]-rp[1]))

        return result
    
    expression = equation.split(" ")
    possibilities = parenthesize(expression)

    max_sum = 0
    for p in possibilities:
        if p[1] > max_sum:
            max_sum = p[1]

    max_expressions = []
    for p in possibilities:
        if p[1] == max_sum:
            max_expressions.append(p[0] + ' = ' + str(p[1]))

    return max_expressions

equation = "3 - 13 - 17 - 7 - 5 - 10"
equations = find_max_parenthesized_expression(equation)
for equation in equations:
    print(equation)