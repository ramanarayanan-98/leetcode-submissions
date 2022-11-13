class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if ch in ["(","{","["]:
                stack.append(ch)
                continue
            if not len(stack):
                return False
            
            if (stack[-1] == "{" and ch == "}") or \
            (stack[-1] == "[" and ch == "]") or \
            (stack[-1] == "(" and ch == ")"):
                stack.pop()
            else:
                return False
        
        return not len(stack)
            