import numpy as np
import pandas as pd

#Alex's fibonacci
def fib_n(n):
    if n == 0 or n ==1:  # Base case
        return n
    return fib_n(n - 1) + fib_n(n - 2)

def fib_seq(n):
    return np.array([fib_n(i) for i in range(n)])

# In this file, you'll put all the functions for creating the Fibonacci sequence up to a certain number.
