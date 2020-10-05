from multiprocessing import Process, Value, Array

def func(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)           # 'd' indicates a double precision float; 
    arr = Array('i', range(10))     # 'i' indicates a signed integer.

    p = Process(target=func, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
