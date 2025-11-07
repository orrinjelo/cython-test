# main.py
import time, timeit
from sum_of_squares import fast_sum_of_squares

start = time.time()
result = fast_sum_of_squares(20000)

print("timeit:", timeit.timeit(
        lambda: fast_sum_of_squares(20000),
        number=1))