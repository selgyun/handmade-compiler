from collections import deque
import Syntax_Analyzer.table as table
import sys


# Load reduce, slr and convert tables
reduce = table.reduce
syntax_analyzer = table.syntax_analyzer
convert_token = table.convert_token
input_token = deque()


#           -*-    How to syntax analyzer works    -*-
# 1. Open the output file from lexical analyzer
# 2. Rename the token so it can be used in the syntax analyzer
# 3. These tokens are put into a deque called "input_token"
# 4. Insert the starting state 0 into the "stack"
# 5. According to the state at the top of the current stack, the action is set according to the slr table.
#     5.1 if action is list,
#         5.1.1 if action[0] is shift, pop left for "input_token" and push it to "stack"
#         5.1.2 if action[0] is reduce, pop for "stack" until meet the condition reduce[action[1]] and push reduce value
#     5.2 if action is not list, push next state(this is action) to the "stack"
#     5.3 else reject
# 6. Repeat 5. until action is accepted area


def parser(filePath):
    f = open(filePath.split(".")[0] + "_lexer_output.txt", "r")
    # Convert the tokens in the lexical analyzer to the terms we want using convert_token(table)
    for tokens in f:
        token = tokens.split(" ")
        # print(token)
        line = token.pop(0)
        value = token.pop().strip()
        # Separation of token and value
        while len(token) > 2:
            value = token.pop().strip()
        token = " ".join(token)
        # Handle arithmetic operators and keywords
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
    # Insert terminating character
    input_token.append((input_token[len(input_token) - 1][0] + 1, "$"))
    # Insert starting state into the "stack"
    stack = deque()
    stack.append(0)
    action = ""

    while action != "acc":
        print(stack)
        # check where the current state is and load the action form the slr table
        # else reject and show where error occurred.
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
        # check action is list or not
        if isinstance(action, list):
            #  we don't have to qualify left substring every time because we put in state in stack
            # it imply left substring is viable prefix if it has rule in str table
            # do shift
            if action[0] == "s":
                stack.append(input_token.popleft()[1])
                stack.append(action[1])
            # do reduce
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
        # do "goto" action
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