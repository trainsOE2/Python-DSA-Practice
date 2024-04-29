prev2 = 0
prev1 = 1
print(prev2)
print(prev1)

def fibonacci(prev2, prev1):
    newFibo = prev2 + prev1
    if newFibo < 1000:
        print(newFibo)
        fibonacci(prev1, newFibo)

fibonacci(prev2, prev1)
