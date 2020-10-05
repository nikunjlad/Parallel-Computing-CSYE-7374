## check how to parallel by Process 
## check pid on master process and child processes. 

from multiprocessing import Process
import os

def print_func(continent='Asia'):
    print('Run child process %s (%s)...' % (continent, os.getpid()))
    print('The name of continent is : ', continent)

if __name__ == "__main__":                    # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func, args=('names',))  # instantiating without any argument
    procs.append(proc)
    print('Child process will start.')
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        print('In main, process %s (%s)...' % os.getpid())
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()


