 bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of open brackets
    stack = []

    for char in s:
        if char in bracket_map.values():  # Check if it's an open bracket
            stack.append(char)
        elif char in bracket_map.keys():  # Check if it's a closing bracket
            if stack and stack[-1] == bracket_map[char]:  # Check if the last open matches
                stack.pop()  # Remove the last open bracket
            else:
                return False  # Mismatched or unbalanced
    return not stack  # Valid if stack is empty at the end