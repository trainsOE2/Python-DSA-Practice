prev2 = 0
prev1 = 1

print(prev2)
print(prev1)

count = 2

n = 11

def fibonacci(prev2, prev1):
    global count
    newFibo = prev2 + prev1
    count = count + 1
    print(newFibo)
    if(count < n):
        fibonacci(prev1, newFibo)

fibonacci(prev2, prev1)