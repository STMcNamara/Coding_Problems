fib_num = 2
fib_prev = 1
even_sum = 2

while fib_num < 4000000:
    fib_mem = fib_num
    fib_num = fib_num + fib_prev
    fib_prev = fib_mem

    if fib_num % 2 == 0:
        even_sum += fib_num

print even_sum
