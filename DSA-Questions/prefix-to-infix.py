OPERATORS = set(['+','-','/','*','(',')','%','^'])
def prefix_to_infix(expression):
    stack = []
    for ch in expression[::-1]:
        if ch not in OPERATORS:
            stack.append(ch)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append("("+val1+ch+val2+")")
    return stack.pop()

print(prefix_to_infix("*-A/BC-/AKL"))
