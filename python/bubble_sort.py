sequence = [4, 3, 5, 0, 1]
swaps = 0
run = True
result = []

# Your Code Here
while run:
    run = False
    for i, x in enumerate(sequence):
        if i == len(sequence)-1:
            break
        if sequence[i] > sequence[i+1]:
            temp = sequence[i]
            sequence[i] = sequence[i+1]
            sequence[i+1] = temp
            run = True
            swaps += 1
        #print(sequence,run)

result = sequence

print(f"Final result: {result}")
print(f"Swaps: {swaps}")
