def evaluatePostfix(expression):
    stack = []
    for ch in expression:
        if ch.isdigit():
            stack.append(ch)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(str(eval(val2+ch+val1)))
    return stack[0]

print(evaluatePostfix("231*+9-"))
