## how to affect the results when start() and join() in different location.

from multiprocessing import Process
import os

# child process
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # create a child process
    #p.start()
    #p.join()
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


