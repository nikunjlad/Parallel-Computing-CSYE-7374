from multiprocessing import Process,Queue
import os

def run_proc(name,q):
    print('Run Child process %s (%s)' % (name, os.getpid()))
    q.put('value')

def run_proce(name,q):
    print('Run Child process %s (%s)' % (name, os.getpid()))
    print(q.get())

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    q = Queue()
    p = Process(target=run_proc,args=('test1',q))
    p2 = Process(target=run_proce,args=('test2',q))
    print('Child Process will start')
    p.start()
    p.join()
    p2.start()
    p2.join()
    print('Child process end.')

