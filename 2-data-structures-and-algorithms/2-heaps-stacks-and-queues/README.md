# Stacks

Operations are performed LIFO (last in, first out), which means that the last element added will be the first one removed. A stack can be implemented using an array or a linked list. If the stack runs out of memory, it’s called a stack overflow.

In the script [stack](./scripts/stack.py) has the representation of the stack in Python

Output of [stack](./scripts/stack.py):

```
Initial stack
['a', 'b', 'c']

Elements popped from stack:
c
b
a

Stack after elements are popped:
[]
```

# Queue

Operations are performed FIFO (first in, first out), which means that the first element added will be the first one removed. A queue can be implemented using an array.

In the script [queue](./scripts/queue.py) has the representation of the min heap in Python

Output of [queue](./scripts/queue.py):

```
Initial queue
['a', 'b', 'c']

Elements dequeued from queue
a
b
c

Queue after removing elements
[]
```

# Heap

A tree-based data structure in which the value of a parent node is ordered in a certain way with respect to the value of its child node(s). A heap can be either a min heap (the value of a parent node is less than or equal to the value of its children) or a max heap (the value of a parent node is greater than or equal to the value of its children).

In the script [min heap](./scripts/min_heap.py) has the representation of the min heap in Python

Output of [min heap](./scripts/min_heap.py):

```
The minHeap is
 PARENT : 3 LEFT CHILD : 5 RIGHT CHILD : 6
 PARENT : 5 LEFT CHILD : 9 RIGHT CHILD : 84
 PARENT : 6 LEFT CHILD : 19 RIGHT CHILD : 17
 PARENT : 9 LEFT CHILD : 22 RIGHT CHILD : 10
The Min val is 3
```

In the script [max heap](./scripts/max_heap.py) has the representation of the max heap in Python

Output of [max heap](./scripts/max_heap.py):

```
The maxHeap is
 PARENT : 84 LEFT CHILD : 22 RIGHT CHILD : 19
 PARENT : 22 LEFT CHILD : 17 RIGHT CHILD : 10
 PARENT : 19 LEFT CHILD : 5 RIGHT CHILD : 6
 PARENT : 17 LEFT CHILD : 3 RIGHT CHILD : 9
The Max val is 84
```

<!-- https://www.geeksforgeeks.org/stack-in-python/ -->
