# reversing a linked list

class Node:
    def __init__(self, value=0, nxt=None):
        self.value = value      
        self.next = nxt

def reverse_linked_list(head):
    prev_node = None
    current = head
    
    while current is not None:  
        # Save the next thing before we lose it
        temp_next = current.next
        
        # flip the pointer
        current.next = prev_node
        
        # move both pointers ahead
        prev_node = current
        current = temp_next

        # print debug info 
        # print(f"Reversed {prev_node.value} -> ...")
    
    return prev_node   # this will be the new head


if __name__ == "__main__":
    # just building a tiny list manually
    head = Node(1, Node(2, Node(3)))
    
    print("Original order: 1 -> 2 -> 3")
    new_head = reverse_linked_list(head)
    
    print("Reversed order:", end=" ")
    curr = new_head
    while curr:
        print(curr.value, end=" -> " if curr.next else "")
        curr = curr.next
    print()  
