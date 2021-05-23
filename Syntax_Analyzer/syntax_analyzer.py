from collections import deque
import table

reduce = table.reduce
syntax_analyzer = table.syntax_analyzer
# class a{int b;} # int id(){a = "hello world"; return "hello";}
test = deque(["vtype", "id", "lparen", "vtype", "id", "comma", "vtype", "id", "rparen", "lbrace", "id", "assign", "literal", "semi", "return", "literal", "semi", "rbrace"])
test.append("$")
stack = deque()
stack.append(0)
action = ""
while action != "acc":
    print(stack)
    if str(stack[-1]).isdigit():
        if test[0] in syntax_analyzer[stack[-1]]:
            action = syntax_analyzer[stack[-1]][test[0]]
        else:
            print("rejected")
            exit(0)
    else:
        if stack[-1] in syntax_analyzer[stack[-2]]:
            action = syntax_analyzer[stack[-2]][stack[-1]]
        else:
            print("rejected")
            exit(0)
    if isinstance(action, list):
        if action[1] == "S":
            stack.append(test.popleft())
            stack.append(action[0])
        else:
            if "" in reduce[action[0]]:
                stack.append(reduce[action[0]][""])
            else:
                tmp = deque()
                while ' '.join(tmp) not in reduce[action[0]]:
                    t = str(stack.pop())
                    if t.isalpha():
                        tmp.appendleft(t)
                stack.append(reduce[action[0]][' '.join(tmp)])
    else:
        stack.append(action)
print("accepted!")
