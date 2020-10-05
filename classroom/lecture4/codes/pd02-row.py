# Row-wise Operation

import numpy as np
import pandas as pd
import multiprocessing as mp

df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
#print(df.head())

def funcs(row):
    returw round(row[1]**2 + row[2]**2, 2)**0.5

with mp.Pool(4) as pool:
    result = pool.imap(funcs, df.itertuples(name=False), chunksize=10)
    output = [round(x, 2) for x in result]

print(output)

