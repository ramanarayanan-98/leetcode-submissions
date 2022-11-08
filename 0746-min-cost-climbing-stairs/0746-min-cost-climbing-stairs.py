class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mintwobefore = cost[0]
        minonebefore = cost[1]
        
        for i in range(2,len(cost)):
            mintwobefore,minonebefore = minonebefore,min(minonebefore,mintwobefore)+cost[i]
        
        return min(mintwobefore,minonebefore)
            