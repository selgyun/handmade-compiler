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
    22: {"comma vtype id MOREARGS": "MOREARGS"},
    23: {"": "MOREARGS"},
    24: {"STMT BLOCK": "BLOCK"},
    25: {"": "BLOCK"},
    26: {"VDECL": "STMT"},
    27: {"ASSIGN semi": "STMT"},
    28: {"if lparen COND rparen lbrace BLOCK rbrace ELSE": "STMT"},
    29: {"while lparen COND rparen lbrace BLOCK rbrace": "STMT"},
    30: {"C comp COND": "COND"},
    31: {"C": "COND"},
    32: {"boolstr": "C"},
    33: {"else lbrace BLOCK rbrace": "ELSE"},
    34: {"": "ELSE"},
    35: {"return RHS semi": "RETURN"},
    36: {"class id lbrace ODECL rbrace": "CDECL"},
    37: {"VDECL ODECL": "ODECL"},
    38: {"FDECL ODECL": "ODECL"},
    39: {"": "ODECL"},
}

syntax_analyzer = {
    0: {
        "vtype": ["s", 6],
        "class": ["s", 5],
        "$": ["r", 4],
        "CODE": 1,
        "VDECL": 4,
        "FDECL": 3,
        "CDECL": 2,
    },
    1: {
        "$": "acc",
    },
    2: {
        "vtype": ["s", 6],
        "class": ["s", 5],
        "$": ["r", 4],
        "CODE": 7,
        "VDECL": 4,
        "FDECL": 3,
        "CDECL": 2,
    },
    3: {
        "vtype": ["s", 6],
        "class": ["s", 5],
        "$": ["r", 4],
        "CODE": 8,
        "VDECL": 4,
        "FDECL": 3,
        "CDECL": 2,
    },
    4: {
        "vtype": ["s", 6],
        "class": ["s", 5],
        "$": ["r", 4],
        "CODE": 9,
        "VDECL": 4,
        "FDECL": 3,
        "CDECL": 2,
    },
    5: {
        "id": ["s", 10],
    },
    6: {
        "id": ["s", 11],
        "ASSIGN": 12,
    },
    7: {
        "$": ["r", 1],
    },
    8: {
        "$": ["r", 2],
    },
    9: {
        "$": ["r", 3],
    },
    10: {
        "lbrace": ["s", 13],
    },
    11: {
        "semi": ["s", 15],
        "assign": ["s", 16],
        "lparen": ["s", 14],
    },
    12: {
        "semi": ["s", 17],
    },
    13: {
        "vtype": ["s", 6],
        "rbrace": ["r", 39],
        "VDECL": 19,
        "FDECL": 20,
        "ODECL": 18,
    },
    14: {
        "vtype": ["s", 22],
        "rparen": ["r", 21],
        "ARG": 21,
    },
    15: {
        "vtype": ["r", 5],
        "id": ["r", 5],
        "rbrace": ["r", 5],
        "if": ["r", 5],
        "while": ["r", 5],
        "return": ["r", 5],
        "class": ["r", 5],
        "$": ["r", 5],
    },
    16: {
        "id": ["s", 31],
        "literal": ["s", 25],
        "character": ["s", 26],
        "boolstr": ["s", 27],
        "lparen": ["s", 30],
        "num": ["s", 32],
        "RHS": 23,
        "EXPR": 24,
        "T": 28,
        "F": 29,
    },
    17: {
        "vtype": ["r", 6],
        "id": ["r", 6],
        "rbrace": ["r", 6],
        "if": ["r", 6],
        "while": ["r", 6],
        "return": ["r", 6],
        "class": ["r", 6],
        "$": ["r", 6],
    },
    18: {
        "rbrace": ["s", 33],
    },
    19: {
        "vtype": ["s", 6],
        "rbrace": ["r", 39],
        "VDECL": 19,
        "FDECL": 20,
        "ODECL": 34,
    },
    20: {
        "vtype": ["s", 6],
        "rbrace": ["r", 39],
        "VDECL": 19,
        "FDECL": 20,
        "ODECL": 35,
    },
    21: {
        "rparen": ["s", 36],
    },
    22: {
        "id": ["s", 37],
    },
    23: {
        "semi": ["r", 7],
    },
    24: {
        "semi": ["r", 8],
    },
    25: {
        "semi": ["r", 9],
    },
    26: {
        "semi": ["r", 10],
    },
    27: {
        "semi": ["r", 11],
    },
    28: {
        "semi": ["r", 13],
        "addsub": ["s", 38],
        "rparen": ["r", 13],
    },
    29: {
        "semi": ["r", 15],
        "addsub": ["r", 15],
        "multdiv": ["s", 39],
        "rparen": ["r", 15],
    },
    30: {
        "id": ["s", 31],
        "lparen": ["s", 30],
        "num": ["s", 32],
        "EXPR": 40,
        "T": 28,
        "F": 29,
    },
    31: {
        "semi": ["r", 17],
        "addsub": ["r", 17],
        "multdiv": ["r", 17],
        "rparen": ["r", 17],
    },
    32: {
        "semi": ["r", 18],
        "addsub": ["r", 18],
        "multdiv": ["r", 18],
        "rparen": ["r", 18],
    },
    33: {
        "vtype": ["r", 36],
        "class": ["r", 36],
        "$": ["r", 36],
    },
    34: {
        "rbrace": ["r", 37],
    },
    35: {
        "rbrace": ["r", 38],
    },
    36: {
        "lbrace": ["s", 41],
    },
    37: {
        "rparen": ["r", 23],
        "comma": ["s", 43],
        "MOREARGS": 42,
    },
    38: {
        "id": ["s", 31],
        "lparen": ["s", 30],
        "num": ["s", 32],
        "EXPR": 44,
        "T": 28,
        "F": 29,
    },
    39: {
        "id": ["s", 31],
        "lparen": ["s", 30],
        "num": ["s", 32],
        "T": 45,
        "F": 29,
    },
    40: {
        "rparen": ["s", 46],
    },
    41: {
        "vtype": ["s", 53],
        "id": ["s", 54],
        "rbrace": ["r", 25],
        "if": ["s", 51],
        "while": ["s", 52],
        "return": ["r", 25],
        "VDECL": 49,
        "ASSIGN": 50,
        "BLOCK": 47,
        "STMT": 48,
    },
    42: {
        "rparen": ["r", 20],
    },
    43: {
        "vtype": ["s", 55],
    },
    44: {
        "semi": ["r", 12],
        "rparen": ["r", 12],
    },
    45: {
        "semi": ["r", 14],
        "addsub": ["r", 14],
        "rparen": ["r", 14],
    },
    46: {
        "semi": ["r", 16],
        "addsub": ["r", 16],
        "multdiv": ["r", 16],
        "rparen": ["r", 16],
    },
    47: {
        "return": ["s", 57],
        "RETURN": 56,
    },
    48: {
        "vtype": ["s", 53],
        "id": ["s", 54],
        "rbrace": ["r", 25],
        "if": ["s", 51],
        "while": ["s", 52],
        "return": ["r", 25],
        "VDECL": 49,
        "ASSIGN": 50,
        "BLOCK": 58,
        "STMT": 48,
    },
    49: {
        "vtype": ["r", 26],
        "id": ["r", 26],
        "rbrace": ["r", 26],
        "if": ["r", 26],
        "while": ["r", 26],
        "return": ["r", 26],
    },
    50: {
        "semi": ["s", 59],
    },
    51: {
        "lparen": ["s", 60],
    },
    52: {
        "lparen": ["s", 61],
    },
    53: {
        "id": ["s", 62],
        "ASSIGN": 12,
    },
    54: {
        "assign": ["s", 16],
    },
    55: {
        "id": ["s", 63],
    },
    56: {
        "rbrace": ["s", 64],
    },
    57: {
        "id": ["s", 31],
        "literal": ["s", 25],
        "character": ["s", 26],
        "boolstr": ["s", 27],
        "lparen": ["s", 30],
        "num": ["s", 32],
        "RHS": 65,
        "EXPR": 24,
        "T": 28,
        "F": 29,
    },
    58: {
        "rbrace": ["r", 24],
        "return": ["r", 24],
    },
    59: {
        "vtype": ["r", 27],
        "id": ["r", 27],
        "rbrace": ["r", 27],
        "if": ["r", 27],
        "while": ["r", 27],
        "return": ["r", 27],
    },
    60: {
        "boolstr": ["s", 68],
        "COND": 66,
        "C": 67,
    },
    61: {
        "boolstr": ["s", 68],
        "COND": 69,
        "C": 67,
    },
    62: {
        "semi": ["s", 15],
        "assign": ["s", 16],
    },
    63: {
        "rparen": ["r", 23],
        "comma": ["s", 43],
        "MOREARGS": 70,
    },
    64: {
        "vtype": ["r", 19],
        "rbrace": ["r", 19],
        "class": ["r", 19],
        "$": ["r", 19],
    },
    65: {
        "semi": ["s", 71],
    },
    66: {
        "rparen": ["s", 72],
    },
    67: {
        "rparen": ["r", 31],
        "comp": ["s", 73],
    },
    68: {
        "rparen": ["r", 32],
        "comp": ["r", 32],
    },
    69: {
        "rparen": ["s", 74],
    },
    70: {
        "rparen": ["r", 22],
    },
    71: {
        "rbrace": ["r", 35],
    },
    72: {
        "lbrace": ["s", 75],
    },
    73: {
        "boolstr": ["s", 68],
        "COND": 76,
        "C": 67,
    },
    74: {
        "lbrace": ["s", 77],
    },
    75: {
        "vtype": ["s", 53],
        "id": ["s", 54],
        "rbrace": ["r", 25],
        "if": ["s", 51],
        "while": ["s", 52],
        "return": ["r", 25],
        "VDECL": 49,
        "ASSIGN": 50,
        "BLOCK": 78,
        "STMT": 48,
    },
    76: {
        "rparen": ["r", 30],
    },
    77: {
        "vtype": ["s", 53],
        "id": ["s", 54],
        "rbrace": ["r", 25],
        "if": ["s", 51],
        "while": ["s", 52],
        "return": ["r", 25],
        "VDECL": 49,
        "ASSIGN": 50,
        "BLOCK": 79,
        "STMT": 48,
    },
    78: {
        "rbrace": ["s", 80],
    },
    79: {
        "rbrace": ["s", 81],
    },
    80: {
        "vtype": ["r", 34],
        "id": ["r", 34],
        "rbrace": ["r", 34],
        "if": ["r", 34],
        "while": ["r", 34],
        "else": ["s", 83],
        "return": ["r", 34],
        "ELSE": 82,
    },
    81: {
        "vtype": ["r", 29],
        "id": ["r", 29],
        "rbrace": ["r", 29],
        "if": ["r", 29],
        "while": ["r", 29],
        "return": ["r", 29],
    },
    82: {
        "vtype": ["r", 28],
        "id": ["r", 28],
        "rbrace": ["r", 28],
        "if": ["r", 28],
        "while": ["r", 28],
        "return": ["r", 28],
    },
    83: {
        "lbrace": ["s", 84],
    },
    84: {
        "vtype": ["s", 53],
        "id": ["s", 54],
        "rbrace": ["r", 25],
        "if": ["s", 51],
        "while": ["s", 52],
        "return": ["r", 25],
        "VDECL": 49,
        "ASSIGN": 50,
        "BLOCK": 85,
        "STMT": 48,
    },
    85: {
        "rbrace": ["s", 86],
    },
    86: {
        "vtype": ["r", 33],
        "id": ["r", 33],
        "rbrace": ["r", 33],
        "if": ["r", 33],
        "while": ["r", 33],
        "return": ["r", 33],
    },
    "acc": {},
}


convert_token = {
    "SINGLE CHARACTER": "character",
    "VARIABLE TYPE": "vtype",
    "SIGNED INTEGER": "num",
    "BOOLEAN STRING": "boolstr",
    "ARITHMETIC OPERATOR": ["addsub", "multdiv"],
    "ASSIGNMENT OPERATOR": "assign",
    "COMPARISON OPERATOR": "comp",
    "TERMINATING SYMBOL": "semi",
    "LPAREN": "lparen",
    "RPAREN": "rparen",
    "LBRACE": "lbrace",
    "RBRACE": "rbrace",
    "COMMA": "comma",
    "LITERAL STRING": "literal",
    "IDENTIFIER": "id",
    "KEYWORD": ["if", "else", "while", "class", "return"],
}