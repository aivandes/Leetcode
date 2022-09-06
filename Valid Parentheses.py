class Solution:
    def isValid(self, s: str) -> bool:
        
        closed = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            
            if char not in closed:
                stack.append(char)
                
            else:
                if not stack:
                    return False
                if stack[-1] != closed[char]:
                    return False
                stack.pop()
        return False if stack else True
