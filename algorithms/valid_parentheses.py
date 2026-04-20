# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(s):
    brackets_map = {
    ")": "(",
    "]": "[",
    "}": "{"
    }
    stack = []
    for bracket in s:
        if bracket not in brackets_map:
            stack.append(bracket)
        elif not stack:
            return False
        else:    
            last_el = stack.pop()
            if last_el != brackets_map.get(bracket):
                return False
    return not stack

if __name__ == "__main__":
    s = "[]"
    assert isValid(s) is True
    s = "[(])]"
    assert isValid(s) is False
    print("Tests passed!")