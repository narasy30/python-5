
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)
number = int(input("Please enter the Fibonacci number range: "))
sum_fib = 0
for num in range(number):
    fib_num = fibonacci(num)
    print(fib_num, end=" ")
    sum_fib += fib_num
print("\nThe sum of Fibonacci series numbers = %d" % sum_fib)
