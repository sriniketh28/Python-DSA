OPERATORS = set(['+','-','/','*','(',')','%','^'])
def prefix_to_infix(expression):
    stack = []
    for ch in expression:
        if ch not in OPERATORS:
            stack.append(ch)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append("("+val2+ch+val1+")")
    return stack.pop()

print(prefix_to_infix("ab*c+d*e/"))
