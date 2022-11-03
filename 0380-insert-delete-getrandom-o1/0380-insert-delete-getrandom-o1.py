class RandomizedSet:

    def __init__(self):
        self.numIndex = collections.defaultdict(int)
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numIndex:
            return False
        self.numIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numIndex:
            return False
        
        reqIdx = self.numIndex[val]
        lastIdx = len(self.nums)-1
        lastIdxEle = self.nums[lastIdx]
        
        self.nums[reqIdx],self.nums[lastIdx] = self.nums[lastIdx],self.nums[reqIdx]
        
        self.numIndex[lastIdxEle] = reqIdx
        del self.numIndex[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return self.nums[randrange(len(self.nums))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()