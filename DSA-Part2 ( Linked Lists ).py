# ------------------------------------------------------------------- #
# Singly Linked List

class Node: # There is no concept of structures so far what I've learned. We use classes instead of struct to create nodes
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
    
class LinkedList:   # Singly Linked List
    size = 0
    def __init__(self):
        self.head = self.tail = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        LinkedList.size += 1
        if self.tail is None:
            self.tail = self.head
    
    def insert_at_end(self,data):
        n = Node(data,None)
        self.tail.next = n
        self.tail = n
        LinkedList.size += 1
        if self.head is None:
            self.head = self.tail

    def insert_at_index(self,data,index):
        if self.head is None:
            print("Linked List is Empty\n")
            return
        elif index == 0:
            self.insert_at_beginning(data)
        elif index == LinkedList.size:
            self.insert_at_end(data)
        elif index > LinkedList.size:
            print(f"Invalid Index\nChoose Between 0 and {LinkedList.size}")
        else:
            counter = 0
            temp = self.head
            while temp and counter != index - 1:
                temp = temp.next
                counter += 1
            n = Node(data,temp.next)
            temp.next = n
            LinkedList.size += 1

    def Delete(self,data):
        if self.head is None:
            print("Linked List Is Empty\n")
            return
        if data == self.head.data:
            temp = self.head
            self.head = self.head.next
            del temp 
            LinkedList.size -= 1
            return
        temp = self.head
        temp2 = self.head.next
        if temp2 is not None:
            while temp2 and temp2.data != data:
                temp = temp.next
                temp2 = temp2.next
            if temp2 is None:
                print("Data Not Found!\n")
                return
            temp.next = temp2.next
            del temp2
            LinkedList.size -= 1

    def print(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        temp = self.head
        while temp:
            print(f"{temp.data} --> ",end="")
            temp = temp.next
        print("\n")

l = LinkedList()    # Declaring Objects of Classes

while True:
    print("1. Insert At Beginning\n")
    print("2. Insert At Index\n")
    print("3. Insert At End\n")
    print("4. Display\n")
    print("5. Delete\n")
    print("Press Any Other Button To Start Double Linked Lists Program\n")
    op = input("\nChoose: ")
    if op == '1':
        l.insert_at_beginning(input("Data: "))
    elif op == '2':
        l.insert_at_index(input("Data: "),int(input("Index: ")))
    elif op == '3':
        l.insert_at_end(input("Data: "))
    elif op == '4':
        l.print()
    elif op == '5':
        l.Delete(input("Data to Delete: "))
    else:
        for n in range(100):
            print("\n")
        break

# -------------------------------------------------------------------- #
# Doubly Linked Lists

class Node2: # There is no concept of structures so far what I've learned. We use classes instead of struct to create nodes
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class LinkedList2:  # Doubly Linked List
    size = 0
    def __init__(self):
        self.head = self.tail = None
    
    def insert_at_beginning(self,data):
        node = Node2(data,self.head,None)
        self.head = node
        self.head.next.prev = node
        LinkedList2.size += 1
        if self.tail is None:
            self.tail = self.head
        if self.tail.prev is None:
            self.tail.prev = self.head
    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        n = Node2(data,None,self.tail.prev)
        self.tail.next = n
        self.tail = n
        LinkedList2.size += 1
        if self.head is None:
            self.head = self.tail

    def insert_at_index(self,data,index):
        if self.head is None:
            print("Linked List is Empty\n")
            return
        elif index == 0:
            self.insert_at_beginning(data)
            return
        elif index == LinkedList2.size:
            self.insert_at_end(data)
            return
        elif index > LinkedList2.size:
            print(f"Invalid Index\nChoose Between 0 and {LinkedList2.size}")
            return
        else:
            counter = 0
            temp = self.head
            while temp and counter != index - 1:
                temp = temp.next
                counter += 1
            n = Node2(data,temp.next,temp)
            temp.next.prev = n
            temp.next = n
            LinkedList2.size += 1

    def Delete(self,data):
        if self.head is None:
            print("Linked List Is Empty\n")
            return
        if data == self.head.data:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp 
            LinkedList2.size -= 1
            return
        elif data == self.tail.data:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp
            return
        temp = self.head
        while temp and temp.next.data != data:
            temp = temp.next
        if temp is None:
            print("Data Not Found!\n")
            return
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        del temp
        LinkedList2.size -= 1

    def print(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        temp = self.head
        while temp:
            print(f"{temp.data} --> ",end="")
            temp = temp.next
        print("\n")

l = LinkedList2()    # Declaring Objects of Classes

while True:
    print("1. Insert At Beginning\n")
    print("2. Insert At Index\n")
    print("3. Insert At End\n")
    print("4. Display\n")
    print("5. Delete\n")
    print("Press Any Other Button To Start The Exercise\n")
    op = input("\nChoose: ")
    if op == '1':
        l.insert_at_beginning(input("Data: "))
    elif op == '2':
        l.insert_at_index(input("Data: "),int(input("Index: ")))
    elif op == '3':
        l.insert_at_end(input("Data: "))
    elif op == '4':
        l.print()
    elif op == '5':
        l.Delete(input("Data to Delete: "))
    else:
        for n in range(100):
            print("\n")
        break


# -------------------------------------------------------------------- #
# Insert After Value And Remove By Value Functions Included

class Node3: # There is no concept of structures so far what I've learned. We use classes instead of struct to create nodes
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class LinkedList3:  # Doubly Linked List
    size = 0
    def __init__(self):
        self.head = self.tail = None
    
    def insert_at_beginning(self,data):
        node = Node3(data,self.head,None)
        self.head = node
        if self.head.next is not None:
            self.head.next.prev = node
        LinkedList3.size += 1
        if self.tail is None:
            self.tail = self.head
        if self.tail.prev is None:
            self.tail.prev = self.head
    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        n = Node3(data,None,self.tail.prev)
        self.tail.next = n
        self.tail = n
        LinkedList3.size += 1
        if self.head is None:
            self.head = self.tail

    def insert_at_index(self,data,index):
        if self.head is None:
            print("Linked List is Empty\n")
            return
        elif index == 0:
            self.insert_at_beginning(data)
            return
        elif index == LinkedList3.size:
            self.insert_at_end(data)
            return
        elif index > LinkedList3.size:
            print(f"Invalid Index\nChoose Between 0 and {LinkedList3.size}")
            return
        else:
            counter = 0
            temp = self.head
            while temp and counter != index - 1:
                temp = temp.next
                counter += 1
            n = Node3(data,temp.next,temp)
            temp.next.prev = n
            temp.next = n
            LinkedList3.size += 1

    def Delete(self,data):
        if self.head is None:
            print("Linked List Is Empty\n")
            return
        if data == self.head.data:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp 
            LinkedList3.size -= 1
            return
        elif data == self.tail.data:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp
            return
        temp = self.head
        while temp and temp.next.data != data:
            temp = temp.next
        if temp is None:
            print("Data Not Found!\n")
            return
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        del temp
        LinkedList3.size -= 1
    
    def insert_values(self,data_list):
        for n in data_list:
            self.insert_at_end(n)

    def insert_ater_value(self,data_after,data_to_insert):
        if self.head is None:
            print("Linked List is Empty\n")
            return
        else:
            temp = self.head
            while temp and temp.data != data_after:
                temp = temp.next
            if temp is None:
                print("Data Not Found!\n")
                return
            else:
                n = Node3(data_to_insert,temp.next,temp)
                temp.next = n
                LinkedList3.size += 1

    def print(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        temp = self.head
        while temp:
            print(f"{temp.data} --> ",end="")
            temp = temp.next
        print("\n")

l = LinkedList3()    # Declaring Objects of Classes
print("\n\nExercise\n\n")
while True:
    print("1. Insert At Beginning\n")
    print("2. Insert At Index\n")
    print("3. Insert At End\n")
    print("4. Display\n")
    print("5. Delete\n")
    print("6. Insert After Value\n")
    print("7. Insert Multiple Values (List)\n")
    print("Press Any Other Button To Start The Exercise\n")
    op = input("\nChoose: ")
    if op == '1':
        l.insert_at_beginning(input("Data: "))
    elif op == '2':
        l.insert_at_index(input("Data: "),int(input("Index: ")))
    elif op == '3':
        l.insert_at_end(input("Data: "))
    elif op == '4':
        l.print()
    elif op == '5':
        l.Delete(input("Data to Delete: "))
    elif op == '6':
        l.insert_ater_value(input("Data to Put After: "),input("Data To Put: "))
    elif op == '7':
        count = int(input("How Many: "))
        List = []
        for n in range(count):
            List.append(input(">> "))
        l.insert_values(List)
    else:
        for n in range(100):
            print("\n")
        break
