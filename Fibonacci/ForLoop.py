prev2 = 0
prev1 = 1

print(prev2)
print(prev1)

for reps in range(18):
    fibonacciNum = prev2 + prev1
    print(fibonacciNum)
    prev2 = prev1
    prev1 = fibonacciNum

