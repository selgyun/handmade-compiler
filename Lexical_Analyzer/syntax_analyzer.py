from dfa import DFA
from transtable import TransitionTable
from collections import deque

table = TransitionTable()

reduce = {
    0: {"CODE": "S"},
    1: {"CDECL CODE": "CODE"},
    2: {"FDECL CODE": "CODE"},
    3: {"VDECL CODE": "CODE"},
    4: {"": "CODE"},
    5: {"vtype id semi": "VDECL"},
    6: {"vtype ASSIGN semi": "VDECL"},
    7: {"id assign RHS": "ASSIGN"},
    8: {"EXPR": "RHS"},
    9: {"literal": "RHS"},
    10: {"character": "RHS"},
    11: {"boolstr": "RHS"},
    12: {"T addsub EXPR": "EXPR"},
    13: {"T": "EXPR"},
    14: {"F multdiv T": "T"},
    15: {"F": "T"},
    16: {"lparen EXPR rparen": "F"},
    17: {"id": "F"},
    18: {"num": "F"},
    19: {"vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace": "FDECL"},
    20: {"vtype id MOREARGS": "ARG"},
    21: {"": "ARG"},
    22: {"comma vtype id MOREARGS": "MOREARG"},
    23: {"": "MOREARGS"},
    24: {"STMT BLOCK": "BLOCK"},
    25: {"": "BLOCK"},
    26: {"VDECL": "STMT"},
    27: {"ASSIGN semi": "STMT"},
    28: {"if lparen COND rparen lbrace BLOCK rbrace ELSE": "STMT"},
    29: {"while lparen COND rparen lbrace BLOCK rbrace": "STMT"},
    30: {"lparen COND comp COND rparen": "COND"},
    31: {"boolstr": "COND"},
    32: {"else lbrace BLOCK rbrace": "ELSE"},
    33: {"": "ELSE"},
    34: {"return RHS semi": "RETURN"},
    35: {"class id lbrace ODECL rbrace": "CDECL"},
    36: {"VDECL ODECL": "ODECL"},
    37: {"FDECL ODECL": "ODECL"},
    38: {"": "ODECL"},
}

syntax_analyzer = {
    0: {"vtype": [6, "S"], "class": [5, "S"], "$": [4, "R"], "CODE": 1, "VDECL": 4, "FDECL": 3, "CDECL": 2},
    1: {"$": "acc"},
    2: {"vtype": [6, "S"], "class": [5, "S"], "$": [4, "R"], "CODE": 7, "VDECL": 4, "FDECL": 3, "CDECL": 2},
    3: {"vtype": [6, "S"], "class": [5, "S"], "$": [4, "R"], "CODE": 8, "VDECL": 4, "FDECL": 3, "CDECL": 2},
    4: {"vtype": [6, "S"], "class": [5, "S"], "$": [4, "R"], "CODE": 9, "VDECL": 4, "FDECL": 3, "CDECL": 2},
    5: {"id": [10, "S"], },
    6: {"id": [11, "S"], "ASSIGN": 12,},
    7: {"$": [1, "R"]},
    8: {"$": [2, "R"]},
    9: {"$": [3, "R"]},
    10: {"lbrace": [13, "S"]},
    11: {"semi": [15, "S"], "assign": [16, "S"], "lparen": [14, "S"]},
    12: {"semi": [17, "S"]},
    13: {"vtype": [6, "S"], "rbrace": [38, "R"], "VDECL": 19, "FDECL": 20, "ODECL": 18},
    14: {"vtype": [22, "S"], "rparen": [21, "R"], "ARG": 21},
    15: {"vtype": [5, "R"], "id": [5, "R"], "rbrace": [5, "R"], "if": [5, "R"], "while": [5, "R"], "return": [5, "R"], "class": [5, "R"], "$": [5, "R"]},
    16: {"id": [31, "S"], "literal": [25, "S"], "character": [26, "S"], "boolstr": [27, "S"], "lparen": [30, "S"], "num": [32, "S"], "RHS": 23, "EXPR": 24, "T": 28, "F": 29},
    17: {"vtype": [6, "R"], "id": [6, "R"], "rbrace": [6, "R"], "if": [6, "R"], "while": [6, "R"], "return": [6, "R"], "class": [6, "R"], "$": [6, "R"]},
    18: {"rbrace": [33, "S"]},
    19: {"vtype": [6, "S"], "rbrace": [38, "R"],"VDECL": 19, "FDECL": 20, "ODECL": 34},
    20: {"vtype": [6, "S"], "rbrace": [38, "R"],"VDECL": 19, "FDECL": 20, "ODECL": 35},
    21: {"rparen": [36, "S"]},
    22: {"id": [37, "S"]},
    23: {"semi": [7, "R"]},
    24: {"semi": [8, "R"]},
    25: {"semi": [9, "R"]},
    26: {"semi": [10, "R"]},
    27: {"semi": [11, "R"]},
    28: {"semi": [13, "R"], "addsub": [38, "S"], "rparen": [13, "R"]},
    29: {"semi": [15, "R"], "addsub": [15, "R"], "multdiv": [39, "S"], "rparen": [15, "R"]},
    30: {"id": [31, "S"], "lparen": [30, "S"], "num": [32, "S"], "EXPR": 40, "T": 28, "F": 29},
    31: {"semi": [17, "R"], "addsub": [17, "R"], "multdiv": [17, "R"], "rparen": [17, "R"]},
    32: {"semi": [18, "R"], "addsub": [18, "R"], "multdiv": [18, "R"], "rparen": [18, "R"]},
    33: {"vtype": [35, "R"], "class": [35, "R"], "$": [35, "R"]},
    34: {"rbrace": [36, "R"]},
    35: {"rbrace": [37, "R"]},
    36: {"lbrace": [41, "S"]},
    37: {"rparen": [23, "R"], "comma": [43, "S"], "MOREARGS": 42},
    38: {"id": [31, "S"], "lparen": [30, "S"], "num": [32, "S"], "EXPR": 44, "T": 28, "F": 29},
    39: {"id": [31, "S"], "lparen": [30, "S"], "num": [32, "S"], "T": 45, "F": 29},
    40: {"rparen": [46, "S"]},
    41: {"vtype": [53, "S"], "id": [54, "S"], "rbrace": [25, "R"], "if": [51, "S"], "while": [52, "S"], "return": [25, "R"], "VDECL": 49, "ASSIGN": 50, "BLOCK": 47, "STMT": 48},
    42: {"rparen": [20, "R"]},
    43: {"vtype": [55, "S"]},
    44: {"semi": [12, "R"], "rparen": [12, "R"]},
    45: {"semi": [14, "R"], "addsub": [14, "R"], "rparen": [14, "R"]},
    46: {"semi": [16, "R"], "addsub": [16, "R"], "multdiv": [16, "R"], "rparen": [16, "R"]},
    47: {"return": [57, "S"], "RETURN": 56},
    48: {"vtype": [53, "S"], "id": [54, "S"], "rbrace": [25, "R"], "if": [51, "S"], "while": [52, "S"], "return": [25, "R"], "VDECL": 49, "ASSIGN": 50, "BLOCK": 58, "STMT": 48},
    49: {"vtype": [26, "R"], "id": [26, "R"], "rbrace": [26, "R"], "if": [26, "R"], "while": [26, "R"], "return": [26, "R"]},
    50: {"semi": [59, "S"]},
    51: {"lparen": [60, "S"]},
    52: {"lparen": [61, "S"]},
    53: {"id": [62, "S"], "ASSIGN": 12},
    54: {"assign": [16, "S"]},
    55: {"id": [63, "S"]},
    56: {"rbrace": [64, "S"]},
    57: {"id": [31, "S"], "literal": [25, "S"], "character": [26, "S"], "boolstr": [27, "S"], "lparen": [30, "S"], "num": [32, "S"], "RHS": 65, "EXPR": 24, "T": 28, "F": 29},
    58: {"rbrace": [24, "R"], "return": [24, "R"]},
    59: {"vtype": [27, "R"], "id": [27, "R"], "rbrace": [27, "R"], "if": [27, "R"], "while": [27, "R"], "return": [27, "R"]},
    60: {"boolstr": [68, "S"], "lparen": [67, "S"], "COND": 66},
    61: {"boolstr": [68, "S"], "lparen": [67, "S"], "COND": 69},
    62: {"semi": [15, "S"], "assign": [16, "S"]},
    63: {"rparen": [23, "R"], "comma": [43, "S"], "MOREARGS": 70},
    64: {"vtype": [19, "R"], "rbrace": [19, "R"], "class": [19, "R"], "$": [19, "R"]},
    65: {"semi": [71, "S"]},
    66: {"rparen": [72, "S"]},
    67: {"boolstr": [68, "S"], "lparen": [67, "S"], "COND": 73},
    68: {"rparen": [31, "R"], "comp": [31, "R"]},
    69: {"rparen": [74, "S"]},
    70: {"rparen": [22, "R"]},
    71: {"rbrace": [34, "R"]},
    72: {"lbrace": [75, "S"]},
    73: {"comp": [76, "S"]},
    74: {"lbrace": [77, "S"]},
    75: {"vtype": [53, "S"], "id": [54, "S"], "rbrace": [25, "R"], "if": [51, "S"], "while": [52, "S"], "return": [25, "R"], "VDECL": 49, "ASSIGN": 50, "BLOCK": 78, "STMT": 48},
    76: {"boolstr": [68, "S"], "lparen": [67, "S"], "COND": 79},
    77: {"vtype": [53, "S"], "id": [54, "S"], "rbrace": [25, "R"], "if": [51, "S"], "while": [52, "S"], "return": [25, "R"], "VDECL": 49, "ASSIGN": 50, "BLOCK": 80, "STMT": 48},
    78: {"rbrace": [81, "S"]},
    79: {"rparen": [82, "S"]},
    80: {"rbrace": [83, "S"]},
    81: {"vtype": [33, "R"], "id": [33, "R"], "rbrace": [33, "R"], "if": [33, "R"], "while": [33, "R"], "else": [85, "S"], "return": [33, "R"], "ELSE": 84},
    82: {"rparen": [30, "R"], "comp": [30, "R"]},
    83: {"vtype": [29, "R"], "id": [29, "R"], "rbrace": [29, "R"], "if": [29, "R"], "while": [29, "R"], "return": [29, "R"]},
    84: {"vtype": [28, "R"], "id": [28, "R"], "rbrace": [28, "R"], "if": [28, "R"], "while": [28, "R"], "return": [28, "R"]},
    85: {"lbrace": [86, "S"]},
    86: {"vtype": [53, "S"], "id": [54, "S"], "rbrace": [25, "R"], "if": [51, "S"], "while": [52, "S"], "return": [25, "R"], "VDECL": 49, "ASSIGN": 50, "BLOCK": 87, "STMT": 48},
    87: {"rbrace": [88, "S"]},
    88: {"vtype": [32, "R"], "id": [32, "R"], "rbrace": [32, "R"], "if": [32, "R"], "while": [32, "R"], "return": [32, "R"]},
    "acc": {},
}
# class a{int b;} # int id(){a = "hello world"; return "hello";}
test = deque(["vtype", "id", "lparen", "rparen", "lbrace", "vtype", "id", "assign", "literal", "semi", "return", "literal", "semi", "rbrace"])
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
