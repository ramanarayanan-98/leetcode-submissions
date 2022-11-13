class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rs,re,cs,ce = 0,len(matrix)-1,0,len(matrix[0])-1
        
        while rs <= re:
            midr = rs+(re-rs)//2
            
            if target >= matrix[midr][0] and target <= matrix[midr][ce]:
                rs = re = midr
                
                while cs <= ce:
                    midc = cs + (ce-cs)//2
                    
                    if matrix[midr][midc] == target:
                        return True
                    elif target > matrix[midr][midc]:
                        cs = midc+1
                    else:
                        ce = midc-1
                
                return False
            
            elif target > matrix[midr][ce]:
                rs = midr+1
            elif target < matrix[midr][0]:
                re = midr-1
        
        return False
            