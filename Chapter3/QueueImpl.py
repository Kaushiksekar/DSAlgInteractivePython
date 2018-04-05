from Queue import Queue

q = Queue()
print("Size : "+str(q.size()))
q.enqueue(12)
print(q.isEmpty())
q.enqueue(13)
q.dequeue()
print(q.size())
