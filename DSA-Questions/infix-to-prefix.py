OPERATORS = set(['+','-','/','*','(',')','%','^'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}

def infix_to_postfix(expression):
    stack = []
    output = ''
    for ch in expression:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output

def infix_to_prefix(expression):
    reverse_infix_expression = list(expression[::-1])
    for i in range(len(reverse_infix_expression)):
        if reverse_infix_expression[i] == "(":
            reverse_infix_expression[i] = ")"
        elif reverse_infix_expression[i] == ")":
            reverse_infix_expression[i] = "("

    return (infix_to_postfix("".join(reverse_infix_expression)))[::-1] 

print(infix_to_prefix("x+y*z/w+u"))
