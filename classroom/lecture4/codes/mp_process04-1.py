
from multiprocessing import Queue

colors = ['red', 'green', 'blue', 'black']
cnt = 1

# instantiating a queue object
queue = Queue()
print('Pushing items to queue:')
for color in colors:
    print('item no: ', cnt, ' ', color)
    queue.put(color)
    cnt += 1

print('\nPopping items from queue:')
cnt = 0
while not queue.empty():
    print('item no: ', cnt, ' ', queue.get())
    cnt += 1

