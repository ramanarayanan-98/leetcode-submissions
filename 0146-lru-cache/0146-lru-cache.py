class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lrudict = dict()
        self.lruhead = None
        self.lrutail = None
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lrudict:
            return -1
        node = self.lrudict[key]
        self.removeNode(node)
        self.addNodeToEnd(node)
        return node.val
        
    def removeNode(self,node):
        if not node:
            return
        
        if node == self.lruhead and node == self.lrutail:
            self.lruhead = None
            self.lrutail = None
        elif node == self.lruhead:
            self.lruhead = self.lruhead.next
            self.lruhead.prev = None
        elif node == self.lrutail:
            self.lrutail = self.lrutail.prev
            self.lrutail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        
    
    def addNodeToEnd(self,node):
        if not self.lruhead and not self.lrutail:
            self.lruhead = self.lrutail = node
            
        else:
            self.lrutail.next = node
            node.prev = self.lrutail
            self.lrutail = node
        
    def put(self, key: int, value: int) -> None:
        if key not in self.lrudict:
            
            if len(self.lrudict) == self.cap:
                valueToDelete = self.lruhead.key
                
                del self.lrudict[valueToDelete]
                self.removeNode(self.lruhead)
                
            node = Node(key,value)
            self.addNodeToEnd(node)
            self.lrudict[key] = node
        else:
            node = self.lrudict[key]
            node.val = value
            self.removeNode(node)
            self.addNodeToEnd(node)
            
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)