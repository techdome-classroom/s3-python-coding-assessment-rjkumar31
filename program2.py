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
            
           class Solution(object):
    def romanToInt(self, s):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        for char in s[::-1]:
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total