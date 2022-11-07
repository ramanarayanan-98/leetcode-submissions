class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost) < 0 :
            return -1
        prevsum,start = 0,-1
        for i in range(len(gas)):
            if prevsum <= 0:
                start = i
                prevsum = gas[i]-cost[i]
            else:
                prevsum += gas[i]-cost[i]
        
        return start
                