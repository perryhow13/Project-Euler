fib_prev = 1
fib_curr = 2
sum_of_even_terms = 0

while fib_curr < 4000000:
  
  if fib_curr % 2 == 0:
    sum_of_even_terms += fib_curr

  temp_curr = fib_curr
  fib_curr = fib_curr + fib_prev
  fib_prev = temp_curr

print sum_of_even_terms
