# queue is a method of lining up items or objects, in real life it's more like a
# of people waiting to use the rest room.
# this process uses a method known by the acronym fIFO - first in, first out
# much like what we have in real life where the first person in a queue is the first to leave

# when working with a list this can have an adverse effect because when we remove one item from a list of 1001 items we'll have a thousand items to move in memory and this can be hard

# to avoid this in python
# we import dequeue module

from collections import deque

# instead of creating an empty queue list, simply surround it with a dequeue method
queue = deque([])
# add items
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# call the popleft method on the queue(NOTE: this is not available on list functions)
queue.popleft()
print(queue)
# check if queue is empty
if not queue:
    print("empty")
