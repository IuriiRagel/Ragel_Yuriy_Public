N_max = int(input("Definne queue size:"))

queue = [0 for _ in range(N_max)]  # initializing list of zeroes
order = 0  # here we will store task number
head = 0  # queue start pointer
tail = 0  # pointer to the element at the end of the queue

def size(): # getting queue size
    if is_empty(): # if the queue is empty
        return 0 # return zero
    elif head == tail: # if the queue is empty, and the pointers match
        return N_max # means that queue is full
    elif head > tail: # if the queue end moved to the start of the list
        return N_max - head + tail
    else: # or if the tail is to the right from the start
        return tail - head

def is_empty(): # check if queue is empty
    # it is empty if pointers match and queue contains a zero
    return head == tail and queue[head] == 0


def add():  # function to add task to the queue
    global tail, order
    order += 1  # increase task number
    queue[tail] = order  # add it to the queue
    print("Task #%d is added" % (queue[tail]))

    # increase pointer by 1 for max module value of element
    # in order to cycle the queue
    tail = (tail + 1) % N_max

def show(): # show priority task
    print("Task #%d is in priority" % (queue[head]))

def do(): # execute priority task
    global head
    print("Task #%d is executed" % (queue[head]))
    queue[head] = 0 # after executing point head to zero
    head = (head + 1) % N_max # and move the pointer further in a cycle

while True:
    cmd = input("Enter the command (add,show,do,exit):")
    if cmd == "empty":
        if is_empty():
            print("Queue is empty")
        else:
            print("There are tasks in the queue")
    elif cmd == "size":
        print("Quantity of tasks in the queue:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("The queue is full")
    elif cmd == "show":
        if is_empty():
            print("The queue is empty")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("The queue is empty")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("The queue is empty. Finishing work now.")
        break
    else:
        print("Incorrect command")