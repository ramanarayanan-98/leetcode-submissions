class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        
        stack = []
        
        for token in tokens:
            stack.append(token)
            # print(token,stack)
            
            while len(stack) > 2 and stack[-1] in ['+','-','*','/'] and\
            stack[-2].lstrip('-').isdigit() and\
            stack[-3].lstrip('-').isdigit():
                operation = stack.pop()
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if operation == '+':
                    stack.append(f"{num1+num2}")
                elif operation == '-':
                    stack.append(f"{num1-num2}")
                elif operation == '*':
                    stack.append(f"{num1*num2}")
                else:
                    stack.append(f"{int(num1/num2)}")
        
        assert len(stack) == 1
        
        return int(stack[0])
                
            
        