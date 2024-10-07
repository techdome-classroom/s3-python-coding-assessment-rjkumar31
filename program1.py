class Solution(object):
    def isValid(self, s):
       
   
        # stack = []

        # # Map of closing brackets to their corresponding opening brackets
        # bracket_map = {
        #     ')': '(',
        #     '}': '{',
        #     ']': '['
        # }

    
        # for char in s:
            
        #     if char in bracket_map:
            
        #         top_element = stack.pop() if stack else '#'
                
                
        #         if bracket_map[char] != top_element:
        #             return False
        #     else:
            
        #         stack.append(char)

        
        # return len(stack) == 0

       def is_valid(s: str) -> bool:
        stack = []
        opening = '({['
        closing = ')}]'
        matches = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

# Example usage
print(is_valid("()"))       # Output: True
print(is_valid("()[]{}"))   # Output: True
print(is_valid("(]"))       # Output: False








    



  

