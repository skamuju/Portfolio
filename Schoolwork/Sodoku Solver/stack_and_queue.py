import copy


class Stack:
    """A last in first out (LIFO) stack representation where elements are pushed and
    popped from the top. Think of a stack of plates, where you can't remove or add a
    plate in the middle, only take from, or add to, the top

    Attributes:
        the_stack - the list that holds the elements of our stack
    """

    def __init__(self, initial=[]):
        """Constructor for a stack
        Set the stack up with the given list if any is provided
        Otherwise, start with an empty list

        Args:
            initial - optional list of elements to fill the stack with
        """
        self.the_stack = copy.copy(initial)

    def __str__(self):
        """String representation of the stack"""
        return "The stack contains: " + str(self.the_stack)

    def is_empty(self):
        """Check if stack has no elements

        Returns:
            True if stack has no elements, False otherwise
        """
        return len(self.the_stack) == 0

    def push(self, element):
        """Add element to top of stack. Does not return anything.

        Args:
            elt - an item to add to the stack
        """
        self.the_stack.append(element)

    def pop(self):
        """Remove and return the top item in the stack (corresponds to the last item in
        the list). Should throw an error if the list is empty.

        Returns:
            the most recently added element
        """
        return self.the_stack.pop()

    def peek(self):
        """Return the top item in the stack (corresponds to the last item in the list)
        but do not remove it. Should throw an error if the list is empty.

        Returns:
            the most recently added element
        """
        return self.the_stack[-1]


class Queue:
    """A first in first out (FIFO) queue representation where elements are added at the
    end of the queue and removed from the front. Think of a line at an amusement park
    where new people join (enqueued) the line at the back and are let in (dequeued) from the
    front

    Attributes:
        the_queue - the list that holds the elements of our queue
    """

    def __init__(self, initial=[]):
        """Constructor for a queue
        Set the queue up with the given list if any is provided
        Otherwise, start with an empty list

        Args:
            initial - optional list of elements to fill the queue with
        """
        self.the_queue = copy.copy(initial)

    def __str__(self):
        """String representation of the queue"""
        return "The queue contains: " + str(self.the_queue)

    def is_empty(self):
        """Check if queue has no elements

        Returns:
            True if queue has no elements, False otherwise
        """
        return len(self.the_queue) == 0

    def enqueue(self, element):
        """Add element to end of queue

        Args:
            elt - an item to add to the queue
        """
        self.the_queue.append(element)

    def dequeue(self):
        """Remove and return the start of the queue (corresponds to the first item in
        the list). Should throw an error if the list is empty.

        Returns:
            the oldest added element
        """
        return self.the_queue.pop(0)

    def peek(self):
        """Return the start of the queue (corresponds to the first item in the list)
        but do not remove it. Should throw an error if the list is empty.

        Returns:
            the most recently added element
        """
        return self.the_queue[0]
