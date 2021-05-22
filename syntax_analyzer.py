from collections import deque
from slr_table import SlrTable
from dfa import SlrDFA


slrTable = SlrTable()
table = slrTable.table
rule = slrTable.rule
alphabet = [value[0] for value in rule.values()] + ["$"]
for value in rule.values():
    alphabet += value[1]
alphaset = set(alphabet)
alphabet = list(alphaset)

slrDFA = SlrDFA("SLR DFA", alphabet, table, 0, 1)

sample_input = (
    "vtype id lparen rparen lbrace id assign literal semi return literal semi rbrace"
)

inputData = sample_input.split()
print(inputData)

parseStack = deque()
parseStack.append(0)

index = 0
while slrDFA.isDone() == False:
    if index < len(inputData):
        inputDatum = inputData[index]
    else:
        inputDatum = "$"
    (running, transition) = slrDFA.run(inputDatum)
    if running and transition[0] == "s":
        parseStack.append(inputDatum)
        parseStack.append(transition[1])
        old = slrDFA.state
        slrDFA.setState(transition[1])
        print(parseStack)
        index += 1
    elif running and transition[0] == "r":

        for i in range(2 * len(rule[transition[1]][1])):
            parseStack.pop()
        tmp = parseStack[-1]
        newState = table[tmp][rule[transition[1]][0]][1]
        parseStack.append(rule[transition[1]][0])
        parseStack.append(newState)
        old = slrDFA.state
        slrDFA.setState(newState)
        print(parseStack)

else:
    print("Parsing done!")