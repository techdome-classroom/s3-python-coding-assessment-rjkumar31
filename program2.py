class Solution(object):
   
    def isValid(self,s):
   
        stack = []

        # Map of closing brackets to their corresponding opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    
        for char in s:
            
            if char in bracket_map:
            
                top_element = stack.pop() if stack else '#'
                
                
                if bracket_map[char] != top_element:
                    return False
            else:
            
                stack.append(char)

        
        return len(stack) == 0


