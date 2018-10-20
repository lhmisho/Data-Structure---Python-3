def bracket(myStr):
    stack = []

    for i in myStr:
        if i == '(':
            stack.append(i)
        if i == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

if __name__=="__main__":
    input_str = input()
    if bracket(input_str):
        print(input_str, "is balanced")
    else:
        print(input_str, "not balanced")