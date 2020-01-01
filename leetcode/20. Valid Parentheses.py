"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        left = {"(", "[", "{"}
        right = {")", "]", "}"}

        stack = []

        for ch in s:
            if ch in left:
                stack.append(ch)
            elif ch in right and stack:
                if ch == "}":
                    if stack.pop() == "{":
                        continue
                    else:
                        return False
                elif ch == "]":
                    if stack.pop() == "[":
                        continue
                    else:
                        return False
                else:
                    if stack.pop() == "(":
                        continue
                    else:
                        return False
            else:
                return False
        if stack:
            return False
        return True