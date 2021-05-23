from collections import deque
import Syntax_Analyzer.table as table
import sys


reduce = table.reduce
syntax_analyzer = table.syntax_analyzer
convert_token = table.convert_token
input_token = deque()


def parser(filePath):
    f = open(filePath, "r")
    for tokens in f:
        token = tokens.split(" ")
        value = token.pop().strip()
        while len(token) > 2:
            value = token.pop().strip()
        token = " ".join(token)
        if token == "ARITHMETIC OPERATOR":
            if value == "+" or value == "-":
                input_token.append(convert_token[token][0])
            else:
                input_token.append(convert_token[token][1])
        elif token == "KEYWORD":
            input_token.append(value)
        else:
            input_token.append(convert_token[token])
    f.close()

    input_token.append("$")
    stack = deque()
    stack.append(0)
    action = ""

    while action != "acc":
        print(stack)
        if str(stack[-1]).isdigit():
            if input_token[0] in syntax_analyzer[stack[-1]]:
                action = syntax_analyzer[stack[-1]][input_token[0]]
            else:
                print("reject!", input_token[0])
                exit(0)
        else:
            if stack[-1] in syntax_analyzer[stack[-2]]:
                action = syntax_analyzer[stack[-2]][stack[-1]]
            else:
                print("reject!", input_token[0])
                exit(0)
        if isinstance(action, list):
            if action[0] == "s":
                stack.append(input_token.popleft())
                stack.append(action[1])
            else:
                if "" in reduce[action[1]]:
                    stack.append(reduce[action[1]][""])
                else:
                    tmp = deque()
                    while " ".join(tmp) not in reduce[action[1]]:
                        t = str(stack.pop())
                        if t.isalpha():
                            tmp.appendleft(t)
                    stack.append(reduce[action[1]][" ".join(tmp)])
        else:
            stack.append(action)
    print("accept!")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        parser(sys.argv[1])
    else:
        parser("output.txt")