class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print(f"Value {key} not found in list.")
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Deleted {key} from the list.")

    def display(self):
        current = self.head
        elems = []
        while current:
            elems.append(str(current.data))
            current = current.next
        print(" -> ".join(elems) if elems else "List is empty.")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print("Initial list:")
    sll.display()

    sll.delete(20)
    print("After deleting 20:")
    sll.display()

    sll.delete(40)  # value not in list
