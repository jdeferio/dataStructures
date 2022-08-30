import typing as t


class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self) -> object:
        self.data: list = []

    def get(self, index: int) -> int:
        try:
            return self.data[index]
        except IndexError:
            return -1

    def addAtHead(self, val: int) -> None:
        self.data.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.data.insert(len(self.data)+1, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if  index<=len(self.data):
            self.data.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        try:
            del self.data[index]
        except IndexError:
            print(f"Index: {index} don't exist")


# Determine if the LL has a cycle, return bool
def hasCycle(self, head: t.Optional[ListNode]) -> bool:
    if head is None:
        return False
    try:
        slow = head.next
        fast = head.next.next
    except AttributeError:
        return False
    
    while slow != fast:
        try:
            slow = slow.next
            fast = fast.next.next
        except AttributeError:
            return False
    return True


def detectCycle(self, head: ListNode) -> ListNode:
    node = head
    check = {}
    while node:
        if node not in check:
            check[node] = 1
        else:
            return node
        node = node.next
    return None


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> t.Optional[ListNode]:
    nodeA = headA
    nodeB = headB
    
    check = {}
    while nodeA:
        if nodeA not in check:
            check[nodeA] = 1
        nodeA = nodeA.next
    
    while nodeB:
        if nodeB in check:
            return nodeB
        nodeB = nodeB.next
    return


def removeNthFromEnd(self, head: t.Optional[ListNode], n: int) -> t.Optional[ListNode]: 
    seen = {}
    node = head
    i = 0
    while node:
        seen[str(i)] = node
        i += 1
        node = node.next
    
    keys = [k for k in seen.keys()]
    
    if len(keys) == 1:
        return
    
    if n == len(keys):
        seen[keys[0]].next = None
        return seen[keys[1]]
    
    if n == 1:
        seen[keys[-(n+1)]].next = None
        return seen[keys[0]]
    
    d = int(keys[-n])
    seen[str(d-1)].next = seen[str(d+1)]
    return seen[keys[0]]


def reverseList(self, head: t.Optional[ListNode]) -> t.Optional[ListNode]:
        if head is None:
            return
        
        nodeStart, node = head, head
        while node and node.next:
            nodeB = node.next
            node.next = nodeB.next
            nodeB.next = nodeStart
            
            nodeStart = nodeB
            
        return nodeStart