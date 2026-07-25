def is_paired(input_string):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for index in input_string:
        if index in "({[":
            stack.append(index)
        elif index in ")}]":
            if not stack or stack[-1] != pairs[index]:
                return False
            stack.pop()
    return len(stack) == 0