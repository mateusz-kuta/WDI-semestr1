

def reverse_linked_list(head):
    previous = None

    # One element exception
    if head.next is None:
        return head

    while head.next is not None:
        # Remember what will be next
        next_head = head.next
        # Update current link to previous
        head.next = previous
        # Set previous to current
        previous = head
        # Set current to next
        head = next_head
    else:
        # Update current head to previous
        head.next = previous

    return head






