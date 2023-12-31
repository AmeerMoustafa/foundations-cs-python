
# A node class that will be reused for a lot of our data structure
# O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A singly linked list class 
# O(n) our worst case is how many nodes we have in our LL.
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        if self.isEmpty():
            print("Linked list is empty, there is nothing to display")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
    
    def add(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            self.size += 1

    def remove(self, value):
        if self.isEmpty():
            print("The list is empty, there is nothing to remove")
        current = self.head
        previous = current
        while current.next != None:
            previous = current
            current = current.next
            if self.head.data == value:
                self.head = self.head.next
                size -= 1
            elif current.data == value:
                previous.next = current.next
                size -= 1
        return print(f"All instances of the number {value} have been removed!")

# A Queue data structure
# O(N) N is the amount of nodes we need to display when calling our display method.
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        if self.isEmpty():
            print("Linked list is empty, there is nothing to display")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
    
    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("The list is empty, there is nothing to remove")
        elif self.size == 1:
            value = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return value
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value

# A stack data structure
# O(1)
class Stack:
    def __init__(self):
        self.head = None
        self.size = 1
    
    def isEmpty(self):
        return self.head == None
    
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            print("The stack is empty, there is nothing to remove")
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value

    def peek(self):
        if self.isEmpty():
            print("The stack is empty, Nothing to see here")
        else:
            print(self.head.data)

# The constructor for our Student object
# O(1)
class Student:
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
    
    def getName(self):
        return self.name
    
    def getMidtermGrade(self):
        return self.midterm_grade
    
    def getFinalGrade(self):
        return self.final_grade
    
    def getAttitude(self):
        return self.good_attitude

# The priority queue data structure that we're going to use to process students
# O(N) N represents the elements we need to add to or remove from our Queue.
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        if self.isEmpty():
            print("The Queue is empty, there is nothing to display")
        else:
            current = self.head
            while current != None:
                print(current.data.getName())
                current = current.next
    
    def enqueue(self, data):

        node = Node(data)

        # if list is empty, just add a node
        if self.isEmpty():
            self.head = node
            self.size += 1
        
        # Check to see if there is only one node in our priority queue
        elif self.size == 1:
            # If only student in queue has false attitude and student to be added has True attitude, put good attitude at head
            if not self.head.data.getAttitude() and node.data.getAttitude():
                node.next = self.head
                self.head = node
                self.size += 1

            # Check if only student in queue and student do be added both have a good attitude
            elif self.head.data.getAttitude() and node.data.getAttitude():
                # Add the student with the highest final grade to the top
                if self.head.data.getFinalGrade() >= node.data.getFinalGrade():
                    self.head.next = node
                    self.size += 1
                else:
                    node.next = self.head
                    self.head = node
                    self.size += 1
            # If both students have a bad attitude, just add the new student to the end of the queue
            else:
                self.head.next = node
                self.size += 1
        # Rest of logic to add when queue has 2 elements.
        else:
            current = self.head
            previous = current
            # if student to be added's attitude is bad, just add it to the end of the list
            if node.data.getAttitude() == False:
                while current.next != None:
                    current = current.next
                current.next = node
                self.size += 1
            else:
                while current != None and current.data.getAttitude():
                    previous = current
                    current = current.next

                previous.next = node
                node.next = current
                self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("The priority queue is empty, nothing to remove")
        elif self.size == 1:
            value = self.head.data
            self.head = None
            self.size -= 1
            return value
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value



# The singly linked list that we're going to be using for the first question
singly_list = LinkedList()

# The stack and queue we're going to be using for our plaindrome problem
plaindrome_stack = Stack()
plaindrome_queue = Queue()

# A priority queue to deal with our students
student_queue = PriorityQueue()
