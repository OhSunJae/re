def is_valid_parentheses(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

print(is_valid_parentheses("(()())"))
print(is_valid_parentheses("((())"))