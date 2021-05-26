from collections import deque
import Syntax_Analyzer.table as table
import sys


reduce = table.reduce
syntax_analyzer = table.syntax_analyzer
convert_token = table.convert_token
input_token = deque()


def parser(filePath):
    f = open(filePath.split(".")[0] + "_lexer_output.txt", "r")
    for tokens in f:
        token = tokens.split(" ")
        # print(token)
        line = token.pop(0)
        value = token.pop().strip()
        while len(token) > 2:
            value = token.pop().strip()
        token = " ".join(token)
        if token == "ARITHMETIC OPERATOR":
            if value == "+" or value == "-":
                input_token.append((int(line), convert_token[token][0]))
            else:
                input_token.append((int(line), convert_token[token][1]))
        elif token == "KEYWORD":
            input_token.append((int(line), value))
        else:
            input_token.append((int(line), convert_token[token]))
    f.close()

    input_token.append((input_token[len(input_token) - 1][0] + 1, "$"))

    stack = deque()
    stack.append(0)
    action = ""

    while action != "acc":
        print(stack)
        if str(stack[-1]).isdigit():
            if input_token[0][1] in syntax_analyzer[stack[-1]]:
                action = syntax_analyzer[stack[-1]][input_token[0][1]]
            else:
                print(
                    "reject at line",
                    input_token[0][0],
                    "and input token is",
                    input_token[0][1],
                )
                exit(1)
        else:
            if stack[-1] in syntax_analyzer[stack[-2]]:
                action = syntax_analyzer[stack[-2]][stack[-1]]
            else:
                print(
                    "reject at line",
                    input_token[0][0],
                    "and input token is",
                    input_token[0][1],
                )
                exit(1)
        if isinstance(action, list):
            if action[0] == "s":
                stack.append(input_token.popleft()[1])
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
    else:
        print("accept!")
        exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        parser(sys.argv[1])
    else:
        parser("output.txt")