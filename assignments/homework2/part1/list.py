from multiprocessing import Pool
import time

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


def f(list_a, list_b):
    x = []
    for elem in list_a:
        x.append([item for item in elem if item in list_b[list_a.index(elem)]])
    return x


if __name__ == '__main__':
    t1 = time.time()
    pool = Pool(processes=4)  # start 4 worker processes

    res = pool.apply(f, (list_a, list_b))
    print("Output: ", res)
    print("Execution time: ", time.time() - t1)
