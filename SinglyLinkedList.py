class Node:
    def __init__(self, data): #constructor to initiate this object
        self.data = data # store data
        self.next = None # store reference (next item)

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def remove(self, data):
        if self.is_empty():
            raise Exception('LinkedList is empty')

        currentNode = self.head()
        previous = None

        while currentNode is not None:
            if currentNode.data == data:
                break
            previous = currentNode
            currentNode = currentNode.next

        if previous:
            previous.next = currentNode.next


    def search(self, data):
        if self.is_empty():
            return "LinkedList is empty"

        searchNode = self.head

        while searchNode is not None:
            if searchNode.data == data:
                return True
            else:
                searchNode = searchNode.next

        return False

    def add_node(self, new_data): #Add nodes here
        addNode = Node(new_data)
        addNode.next = self.head
        self.head = addNode

    def size(self):
        size = 0
        if self.is_empty():
            return 0
        current = self.head
        while current is not None:
            size +=1
            current = current.next
        return size
