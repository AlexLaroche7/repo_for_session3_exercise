import numpy as np
import pandas as pd

# In this file, you'll put all the functions for creating the Fibonacci sequence up to a certain number.
 def Fibonacci(n): 
    if n<= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
