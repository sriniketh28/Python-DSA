def evaluatePrefix(expression):
    stack = []
    for ch in expression[::-1]:
        if ch.isdigit():
            stack.append(ch)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(str(eval(val2+ch+val1)))
    return stack[0]

print(evaluatePrefix("+9*26"))
