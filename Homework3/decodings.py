"""
Author: Aidan Dalgarno-Platt
"""

single_bit_encodings = ['0', '1']
double_bit_encodings = ['10', '01']
triple_bit_encodings = ['111', '011']

binary_string = input()

decodings = [1] # stores previous counts of i - 1 substring dynamic-programming-style
                # starts at 1 because there is one decoding guaranteed from the 1 bit results

for i in range(1, len(binary_string) + 1): # go until len(binary_string) + 1 because the final answer is the subproblem solved after the final bit
    # instead of recursively doing this for i - 1 and setting count equal to that, just use the decodings[i - 1] result we already have
    decodings.append(decodings[i - 1])

    # if the 2 digits are one of the listed decodings, go back recursively starting from i - 2
    # however, instead of doing recursion, instead just use the result from decodings[i - 2]
    # add this result to the total decodings for this subproblem
    if i > 1 and (binary_string[i - 2] + binary_string[i - 1]) in double_bit_encodings:
        decodings[i] += decodings[i - 2]

    # if the 3 digits are one of the listed decodings, go back recursively starting from i - 3
    # however, instead of doing recursion, instead just use the result from decodings[i - 3]
    # add this result to the total decodings for this subproblem
    if i > 2 and (binary_string[i - 3] + binary_string[i - 2] + binary_string[i - 1]) in triple_bit_encodings:
        decodings[i] += decodings[i - 3]

print(decodings[len(decodings) - 1])