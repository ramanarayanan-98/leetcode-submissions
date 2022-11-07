from sortedcontainers import SortedDict
class Solution:
    def decrementCount(self,itemcounts,key):
        if key not in itemcounts:
            return
        itemcounts[key] -= 1
        
        if not itemcounts[key]:
            del itemcounts[key]
            
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        itemcounts = SortedDict()
        for num in hand:
            itemcounts[num] = itemcounts.get(num,0) + 1
        
        while len(itemcounts):
            curkey = list(itemcounts.keys())[0]
            self.decrementCount(itemcounts,curkey)
            count = 1
            while count < groupSize and curkey+1 in itemcounts:
                count += 1
                self.decrementCount(itemcounts,curkey+1)
                curkey += 1
            if count != groupSize:
                return False
        
        return True