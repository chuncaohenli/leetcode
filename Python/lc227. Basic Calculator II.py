# def calculate(s):
#     if not s:
#         return "0"
#     stack, num, sign = [], 0, "+"
#     for i in range(len(s)):
#         if s[i].isdigit():
#             num = num*10+ord(s[i])-ord("0")
#         if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
#             if sign == "-":
#                 stack.append(-num)
#             elif sign == "+":
#                 stack.append(num)
#             elif sign == "*":
#                 stack.append(stack.pop()*num)
#             else:
#                 tmp = stack.pop()
#                 if tmp//num < 0 and tmp%num != 0:
#                     stack.append(tmp//num+1)
#                 else:
#                     stack.append(tmp//num)
#             sign = s[i]
#             num = 0
#     return sum(stack)

def calculate(s):
    stack = []
    sign = '+'
    i = 0
    num = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            j = i + 1
            num = int(c)
            while j < len(s) and s[j].isdigit():
                num = 10 * num + int(s[j])
            i = j - 1
        if c in ['+', '-', '*', '/'] or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            sign = c
        i += 1
        print(i)
    return sum(stack)

print(calculate("123"))