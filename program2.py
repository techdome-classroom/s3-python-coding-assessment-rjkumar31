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
    


