# Parallelizing using Pool.starmap()
import numpy as np
import multiprocessing as mp
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()

def examp01(row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

pool = mp.Pool(4)

results = pool.starmap(examp01, [(row, 4, 8) for row in data])

pool.close()

print('Pool.starmap execution:', results[:10])
