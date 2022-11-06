class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = 1
        for i in range(n-1,-1,-1):
            if c+digits[i] <= 9:
                digits[i] += c
                c = 0
                break
            c = 1
            digits[i] = (digits[i]+c)%10
        
        if c == 1:
            digits.insert(0,1)
        return digits
                
            