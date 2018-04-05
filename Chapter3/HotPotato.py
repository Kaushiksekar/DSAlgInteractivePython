from Queue import Queue

def hotPotato(namelist, num):
    q = Queue()

    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:

        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 3))
