# Parallelizing using Pool.map()
import numpy as np
import multiprocessing as mp
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()

# Redefine, with only 1 mandatory argument.
def examp01_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

pool = mp.Pool(4)

results = pool.map(examp01_rowonly, [row for row in data])

pool.close()

print('Pool.map execution:',results[:10])

