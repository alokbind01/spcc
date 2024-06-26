import re

expr_buffer = []
optm_code = []

with open(r"sample_code_unopt.txt") as source:
    code = source.readlines()
    source.close()

print("\nInput Expressions: \n")
for line in code:
    print(line)

for line in code:
    spline = line.replace(" ", "")
    if "=" in spline:
        expr = (re.findall(r"(\w)+=\S*", spline))
        for y in expr_buffer:
            for x in y:
                if expr[0] == x:
                    expr_buffer.remove(y)

    if "/" in spline:
        expr = (re.findall(r"[a-zA-Z]+[\d]*/[a-zA-Z]+[\d]*", spline))
        for x in expr:
            if x not in expr_buffer:
                expr_buffer.append(x)
                s = "t"+ str(expr_buffer.index(x))
                optm_code.append(s + " = " + x + "\n")
                spline = spline.replace(x, s)
            else:
                s = "t" + str(expr_buffer.index(x))
                spline = spline.replace(x, s)

    if "*" in spline:
        expr = (re.findall(r"[a-zA-Z]+[\d]*\*[a-zA-Z]+[\d]*", spline))
        for x in expr:
            if x not in expr_buffer:
                expr_buffer.append(x)
                s = "t"+ str(expr_buffer.index(x))
                optm_code.append(s + " = " + x + "\n")
                spline = spline.replace(x, s)
            else:
                s = "t" + str(expr_buffer.index(x))
                spline = spline.replace(x, s)

    if "+" in spline:
        expr = (re.findall(r"[a-zA-Z]+[\d]*\+[a-zA-Z]+[\d]*", spline))
        for x in expr:
            if x not in expr_buffer:
                expr_buffer.append(x)
                s = "t"+ str(expr_buffer.index(x))
                optm_code.append(s + " = " + x + "\n")
                spline = spline.replace(x, s)
            else:
                s = "t" + str(expr_buffer.index(x))
                spline = spline.replace(x, s)

    if "-" in spline:
        expr = (re.findall(r"[a-zA-Z]+[\d]*-[a-zA-Z]+[\d]*", spline))
        for x in expr:
            if x not in expr_buffer:
                expr_buffer.append(x)
                s = "t"+ str(expr_buffer.index(x))
                optm_code.append(s + " = " + x + "\n")
                spline = spline.replace(x, s)
            else:
                s = "t" + str(expr_buffer.index(x))
                spline = spline.replace(x, s)

    optm_code.append(spline)

print("\nOptimized Expressions with computed compiler variable assignments: \n")
for line in optm_code:
    print(line)

# input
# sample_code_unopt.txt
# c = a/b * d 
# a = c * d
# f = a/b * c/d + e 
# g = f * a/b - c/d
