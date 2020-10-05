# Column-wise Operation

import numpy as np
import pandas as pd
import multiprocessing as mp

df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
#print(df.head())

def sumfunc(column):
    return sum([i**2 for i in column[1]])

with mp.Pool(2) as pool:
    result = pool.imap(sumfunc, df.iteritems(), chunksize=10)
    output = [x for x in result]

print(output) 

