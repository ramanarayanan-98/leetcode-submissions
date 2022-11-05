class Solution:
    def reverseBits(self, n: int) -> int:
        reversedn = 0
        
        for _ in range(32):
            d = n%2
            n >>= 1
            reversedn = (reversedn << 1)+d
        
        return reversedn