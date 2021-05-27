# handmade-compiler
Implement  the  lexical  analyzer  and  syntax  analyzer  for  a  simplified Java programming language. Finally, implement the compiler.

## Usage

    lex_and_parse.py test2.java
    
## Simplified java
### < Lexical specifications >
* <b>Variable type</b>
  * <b>int</b> for a signed integer
  * <b>char</b> for a single character
  * <b>boolean</b> for a Boolean string
  * <b>String</b> for a literal string
* <b>Signed integer</b>
  * A single zero digit (e.g., 0)
  * A non-empty sequence of digits, starting from a non-zero digit
  * (e.g., 1, 22, 123, 56, … any non-zero positive integers)
  * (e.g., 001 is not allowed)
  * A non-empty sequence of digits, starting from a minus sign symbol and a non-zero digit
  * (e.g., -1, -22, -123, -56, .. any non-zero negative integers)
* <b>Single character</b>
  * A single digit, English letter, block, or any symbol, starting from and terminating with a symbol ‘ (e.g., ‘a’, ‘1’, ‘ ‘, ‘&’)
* <b>Boolean string</b>
  * true and false
* <b>Literal string</b>
  * Any combination of digits, English letters, and blanks, starting from and terminating with a symbol “ (e.g., “Hello world”, “My student id is 12345678”)
* <b>An identifier of variables and functions</b>
  * A non-empty sequence of English letters, digits, and underscore symbols, starting from an English letter or a underscore symbol
  * (e.g., i, j, k, abc, ab_123, func1, func_, __func_bar__)
* <b>Keywords for special statements</b>
  * <b>if</b> for if statement
  * <b>else</b> for else statement
  * <b>while</b> for while statement
  * <b>class</b> for class statement
  * <b>return</b> for return statement
* <b>Arithmetic operators</b>
  * +, -, *, and /
* <b>Assignment operator</b>
  * =
* <b>Comparison operators</b>
  * <, >, ==, !=, <=, and >=
* <b>A terminating symbol of statements</b>
  * ; 
* <b>A pair of symbols for defining area/scope of variables and functions</b>
  * { and }
* <b>A pair of symbols for indicating a function/statement</b>
  * ( and )
* <b>A pair of symbols for using an array</b>
  * [ and ]
* <b>A symbol for separating input arguments in functions</b>
  * ,
* <b>Whitespaces</b>
  * a non-empty sequence of \t, \n, and blank

### < CFG G >
1. S -> CODE
2. CODE -> CDECL CODE 
3. CODE -> FDECL CODE 
4. CODE ->  VDECL CODE 
4. CODE -> ''
4. VDECL -> vtype id semi 
4. VDECL -> vtype ASSIGN semi
4. ASSIGN -> id assign RHS
4. RHS ->   EXPR 
4. RHS -> literal 
4. RHS -> character 
4. RHS -> boolstr
4. EXPR ->  T addsub EXPR
4. EXPR -> T
4. T ->   F multdiv T
4. T -> F
4. F ->   lparen EXPR rparen 
4. F -> id 
4. F -> num
4. FDECL ->  vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
4. ARG ->   vtype id MOREARGS
4. ARG -> ''
4. MOREARGS ->   comma vtype id MOREARGS 
4. MOREARGS -> ''
4. BLOCK ->   STMT BLOCK
4. BLOCK -> ''
4. STMT ->   VDECL 
4. STMT -> ASSIGN semi
4. STMT ->   if lparen COND rparen lbrace BLOCK rbrace ELSE
4. STMT ->   while lparen COND rparen lbrace BLOCK rbrace
4. COND ->   COND comp C
4. C -> COND
4. C -> boolstr
4. ELSE ->   else lbrace BLOCK rbrace 
4. ELSE -> ''
4. RETURN ->   return RHS semi
4. CDECL ->   class id lbrace ODECL rbrace
4. ODECL ->   VDECL ODECL
4. ODECL -> FDECL ODECL 
4. ODECL -> ''
