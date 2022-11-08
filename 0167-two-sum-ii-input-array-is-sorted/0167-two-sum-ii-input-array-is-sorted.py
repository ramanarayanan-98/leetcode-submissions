class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st,end = 0,len(numbers)-1
        
        while st < end:
            curSum = numbers[st]+numbers[end]
            
            if curSum == target:
                return [st+1,end+1]
            if curSum > target:
                end -= 1
            else:
                st += 1
        return [-1,-1]