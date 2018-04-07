from Node import Node

class UnorderedLinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        currentNode = self.head
        while currentNode != None:
            currentNode = currentNode.getNext()
            count += 1

        return count

    def search(self, data):
        current = self.head
        found = False

        while current != None:
            if current.getData() == data:
                found = True
                break
            else:
                current = current.getNext()

        return found

    def remove(self, data):
        found = False
        previous = None
        current = self.head

        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            return str(data)+" is removed from the list"
        elif previous != None and found:
            previous.setNext(current.getNext())
            return str(data)+" is removed from the list"
        else:
            return str(data)+" is not present in the list"
