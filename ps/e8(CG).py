import re

f = open("IntermediateCode.txt", 'r')
lines = f.readlines()
f.close()

fifo_return_reg = 'R0'
reg = [0] * 13
var = {}
store_seq = []
fifo_reg = 0
operator_list = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV', '=': 'MOV', '==': 'NE', '>': 'G', '>=': 'GE', '<': 'L', '<=': 'LE', 'and': 'AND', 'or': 'OR'}

def fifo():
    global fifo_reg
    global fifo_return_reg
    for k, v in var.copy().items():
        if v == 'R' + str(fifo_reg):
            fifo_return_reg = v
            var.pop(k)
            if k in store_seq:
                store_seq.remove(k)
                print("ST", k, ',', v, sep='')
    fifo_reg = int(fifo_return_reg[1:]) + 1
    return fifo_return_reg

def getreg():
    for i in range(0, 13):
        if reg[i] == 0:
            reg[i] = 1
            return 'R' + str(i)
    register = fifo()
    return register

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    line = line.split()
    length = len(line)

    if length == 0:
        continue

    if length == 1:
        print(line[0])
        continue

    if re.match(r'^t[0-9]+$', line[0]):
        continue

    if length == 3:
        lhs = line[0]
        operand = line[2]
        if operand not in var:
            var[operand] = getreg()
            if operand.isalpha():
                print("LD", var[operand], ', ', operand, sep="")
            else:
                print("MOV", var[operand], ', #', operand, sep="")
        if lhs in store_seq:
            old_reg = var[lhs]
            store_seq.remove(lhs)
            print("ST", lhs, ',', old_reg, sep='')
        var[lhs] = var[operand]
        store_seq.append(lhs)

    elif 'goto' in line:
        if 'if' in line:
            operand = line[1]
            label = line[3]
            if operand not in var:
                var[operand] = getreg()
                if operand.isalpha():
                    print("LD", var[operand], ', ', operand, sep="")
                else:
                    print("MOV", var[operand], ', #', operand, sep="")
            print("BNEZ", var[operand], ',', label)
        else:
            print("BR", line[1])

    else:
        if len(line) >= 5:
            oper = line[3]
            operand1 = line[2]
            operand2 = line[4]
            lhs = line[0]
            if operand1 not in var:
                var[operand1] = getreg()
                if operand1.isalpha():
                    print("LD", var[operand1], ', ', operand1, sep="")
                else:
                    print("MOV", var[operand1], ', #', operand1, sep="")
            if operand2 not in var:
                var[operand2] = getreg()
                if operand2.isalpha():
                    print("LD", var[operand2], ', ', operand2, sep="")
                else:
                    print("MOV", var[operand2], ', #', operand2, sep="")
            operator_print = operator_list.get(oper)
            if operator_print:
                if lhs in store_seq:
                    old_reg = var[lhs]
                    store_seq.remove(lhs)
                    print("ST", lhs, ',', old_reg, sep='')
                var[lhs] = getreg()
                store_seq.append(lhs)
                print(operator_print, var[lhs], ',', var[operand1], ',', var[operand2], sep=' ')

        else:
            operand = line[3]
            lhs = line[0]
            if operand not in var:
                var[operand] = getreg()
                if operand.isalpha():
                    print("LD", var[operand], ', ', operand, sep="")
                else:
                    print("MOV", var[operand], ', #', operand, sep="")
            if lhs in store_seq:
                old_reg = var[lhs]
                store_seq.remove(lhs)
                print("ST", lhs, ',', old_reg, sep='')
            var[lhs] = getreg()
            store_seq.append(lhs)
            print("NOT", var[lhs], ',', var[operand], sep='')

for i in store_seq:
    print("ST", i, ',', var[i], sep='')


# input
# IntermediateCode.txt
# a = 10
# b = 9
# t0= 10 + 9
# tl = 19 + 100
# c = 119
# e = 10
# f = 8
# t2 = 10 * 8
# d = 80
# |0:
# t3 = 10 >= 9
# t4 = not 1
# if 0 goto |1
# a = 19
# 15 = 80 * 100
# g = 8000
# |1:
# u = 10
# j = 99
