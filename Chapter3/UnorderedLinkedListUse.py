from UnorderedLinkedList import UnorderedLinkedList

list1 = UnorderedLinkedList()

list1.add(24)
list1.add(35)

print("Size of list1 is "+str(list1.size()))
print("Does element 24 exist? "+str(list1.search(24)))
print("Does element 22 exist? "+str(list1.search(22)))
print(list1.remove(35))
print(list1.remove(235))
