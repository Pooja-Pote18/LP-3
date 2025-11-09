#pratical no 1
def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
print("Fibonacci Series using Recursion:")
n = 10
for i in range(n):
    print(recursive_fibonacci(i))




def non_recursive_fibonacci(n):
    first=0
    second=1
    print(first)
    print(second)
    while n-2>0:
        third = first + second
        first=second
        second=third
        print(third)
        n-=1

print("Fibonacci Series using Non-Recursion:")
n = 10
non_recursive_fibonacci(n)




