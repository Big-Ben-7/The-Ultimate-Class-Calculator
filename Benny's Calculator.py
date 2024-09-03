# %%
from math import *
import cmath
import types

global ans
ans = 0.0
global real
real = 0.0
global imag
imag = 0.0
global imag2
imag2 = 0.0
global mod
mod = 0.0
global ang
ang = 0.0
global sum
sum = 0.0
global rat
rat = 0.0
global dif
dif = 0.0
global root
root = 0.0
global root2
root2 = 0.0
global binsum
binsum = ""
global index
index = 0.0
global keeps
keeps = ["ans", "pi", "e", "tau", "inf", "nan", "infj", "nanj", "keeps", "real", "imag", "imag2", "mod", "ang", "sum", "rat", "root", "root2", "binsum", "dif", "index"]

def clear_variables():
    for var in list(globals()):
        if not var.startswith('_') and var not in keeps and not isinstance(globals()[var], (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, type)):
            del globals()[var]

def print_binomial(a, b, c, d, n, k, unterm, x, y):
    global binsum
    co = comb(abs(n), k) * a ** (abs(n) - k) * c ** k
    xpow = round(b * (abs(n) - k), 12)
    ypow = round(d * k, 12)
    if round(co, 12) == 1 and (xpow != 0 or ypow != 0):
        cost = ""
    elif round(co, 12) == -1 and (xpow != 0 or ypow != 0):
        cost = "-"
    else:
        cost = f"{round(co, 12)} "
    if xpow == 1:
        xpowst = x + " "
    elif xpow == 0:
        xpowst = ""
    else:
        xpowst = x + f"^{xpow} "
    if ypow == 1:
        ypowst = y
    elif ypow == 0:
        ypowst = ""
    else:
        ypowst = y + f"^{ypow}"
    combined = cost + xpowst + ypowst
    if combined[len(combined) - 1] == " ":
        combined = combined[:len(combined) - 1]
    if n >= 0:
        print(f"Term {unterm}: " + combined)
    else:
        print(f"Term {unterm} denominator: " + combined)
    if combined[0] == "-":
        combined = combined[1:]
        binsum = binsum[:len(binsum) - 3] + " - "
    binsum += combined + " + "
    covar = f"coef{unterm}"
    globals()[covar] = co
    keeps.append(covar)
    print(covar+ f" (term {unterm} coefficient) = {round(co, 12)}")
    print()

def from_polar():
    global ans
    global real
    global imag
    global ang
    global mod
    print()
    print("Please enter the modulus/absolute value and angle/argument of the terms")
    while True:
        clear_variables()
        print()
        av = input("Term 1 modulus/absolute value (i for info): ")
        if av == "<" or av == "exit" or av == "exi":
            break
        elif av == "i" or av == "info" or av == "inf":
            print()
            print('Real numbers and expressions, such as "3 * sin(pi / 3)", can be entered as terms')
            print("The following non-parenthesized operators and functions can be entered as part of an expression:")
            print("Operators: + (add), - (subtract), * (multiply), / (divide), // (integer divide), % (remainder), ** (exponent)")
            print("Functions: eg. abs(x), sqrt(x), cbrt(x), pow(x, y), log(x, base), factorial(x), comb(x, y), perm(x, y), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), degrees(x), radians(x), sum([x, y, z,...]), int(x), round(x), etc.")
            print('Real constants such as "pi", "e", and "tau" can be entered')
            print('Real variables can also be entered, for example: "ans" (previous real answer), "real" (real part of previous complex result), "imag" (imaginary part of previous complex result), "root" (1st real solution of previous quadratic), "root2" (2nd real solution of previous quadratic), "imag2" (imaginary part of 2nd previous quadratic complex solution) "sum" (previous series summation), "rat" (previous geometric series common ratio), "dif" (previous arithmetic series common difference), "term1" (1st term of previous series), "coef1" (1st coefficient of previous binomial expansion), and stored variables')
            print("The above operators and functions can only be entered as part of an expression, not as an operation")
            print('Enter "rec" for rectangular form, "r" for real operation, "m" for matrix operation, "f" for function (this will direct to polynomial), "s" for summation (this will direct to binomial expansion)')
            print()
            print("Notes:")
            print("Fractional exponents can be used to root: eg. (-1 + 0i) ^ (1/2 + 0i) = i")
            print('Trigonometric functions accept and output angles in radians. The degrees and radians functions or operations can be used to convert')
            print("The result of trigonometric inverse functions (eg. asin, acos, atan, etc.) will lie in their restricted domains")
            print("Integer divide (//) and int() will remove the decimal part from the output, wheras round() will follow the standard rounding rules: eg. 3 // 2 = int(3 / 2) = 1, but round(3 / 2) = 2")
            print("For more information, visit the python math and operators websites")
            continue
        elif av == "rec" or av == "rectangular" or av == "rectangular form":
            from_rectangular()
            break
        elif av == "r" or av == "real" or av == "rea" or av == "real operation":
            real_operation()
            break
        elif av == "f" or av == "function" or av == "fun":
            polynomial()
            break
        elif av == "m" or av == "matrix" or av == "mat":
            matrix_operation()
            break
        elif av == "s" or av == "sum" or av == "summation":
            binomial_expansion()
            break
        try:
            av = eval(av)
            if round(av, 12) < 0:
                print('Absolute values cannot be negative')
                continue
        except:
            print('Please enter a real nonnegative number or expression, "rec" for rectangular form, "r" for real operation, "m" for matrix operation, "f" for function, "s" for summation, "i" for info, or "<" to exit')
            continue
        inang = input("Term 1 angle/argument: ")
        if inang == "<" or inang == "exit" or inang == "exi":
            continue
        try:
            inang = eval(inang)
        except:
            print('Please enter a real number or expression, or "<" to exit')
            continue
        while True:
            angmode = input("Inputted in radians (r) or degrees (d)? ")
            if angmode == "radians" or angmode == "rad" or angmode == "r":
                ang = inang
                break
            elif angmode == "degrees" or angmode == "deg" or angmode == "d":
                ang = radians(inang)
                break
            else:
                print('Please enter either "r" for radians or "d" for degrees')
        a = av * cos(ang)
        b = av * sin(ang)
        cterm1 = f"{round(av, 12)} cos({round(inang, 12)}) + {round(av, 12)} sin({round(inang, 12)})i"
        print("First term: " + cterm1)
        while True:
            print()
            op = input("Operation (i for info): ")
            if op == "info" or op == "i" or op == "inf":
                print()
                print('The following operations can be entered: equals (=), add (+), subtract (-), multiply (*), divide (/), exponent (^), rectangular (rec)')
                print()
                print("Notes:")
                print('The name, sign, or first 3 letters of any operation can be entered: eg. "absolute value", "abs", and "||" all work.')
                print("Fractional exponents can be used to root: eg. (-1 + 0i) ^ (1/2 + 0i) = i.")
                print('Expressions entered as terms can be operated on or evaluated with the "equals" (=) operation.')
                print("The above operations can only be entered as an operation, not as part of an expression.")
            else:
                break
        if op == "<" or op == "exit" or op == "exi":
            continue
        print()
        if not(op == "=" or op == "equals" or op == "equ" or op == "rectangular" or op == "rec" or op == "rectangular form"):
            av2 = input("Term 2 modulus/absolute value: ")
            if av2 == "<" or av2 == "exit" or av2 == "exi":
                continue
            try:
                av2 = eval(av2)
                if round(av2, 12) < 0:
                    print('Absolute values cannot be negative')
                    continue
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue                        
            inang2 = input("Term 2 angle/argument: ")
            if inang2 == "<" or inang2 == "exit" or inang2 == "exi":
                continue
            try:
                inang2 = eval(inang2)
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue
            while True:
                angmode2 = input("Inputted in radians (r) or degrees (d)? ")
                if angmode2 == "radians" or angmode2 == "rad" or angmode2 == "r":
                    ang2 = inang2
                    break
                elif angmode2 == "degrees" or angmode2 == "deg" or angmode2 == "d":
                    ang2 = radians(inang2)
                    break
                else:
                    print('Please enter either "r" for radians or "d" for degrees')
            c = av2 * cos(ang2)
            d = av2 * sin(ang2)
            cterm2 = f"{round(av2, 12)} cos({round(inang2, 12)}) + {round(av2, 12)} sin({round(inang2, 12)})i"
            print("Second term: " + cterm2)
            print()
        try:
            if op == "=" or op == "equals" or op == "equ":
                res = cmath.polar(complex(a, b))
                ares = res[1]
                while True:
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "+" or angle == "pos" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        ares = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op == "+" or op == "add":
                res = cmath.polar(complex(a, b) + complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "+" or angle == "pos" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        ares = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op == "-" or op == "subtract" or op == "sub":
                res = cmath.polar(complex(a, b) - complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "+" or angle == "pos" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        ares = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op == "*" or op == "multiply" or op == "mul":
                res = cmath.polar(complex(a, b) * complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "+" or angle == "pos" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        ares = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op == "/" or op == "divide" or op == "div":
                res = cmath.polar(complex(a, b) / complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "+" or angle == "pos" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        ares = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op == "^" or op == "exponent" or op == "exp" or op == "**":
                res = cmath.polar(complex(a, b) ** complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "+" or angle == "pos" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        ares = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op == "rectangular" or op == "rec" or op == "rectangular form":
                res = cmath.rect(av, ang)
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                real = res.real
                print(f"real (real part) = {round(real, 12)}")
                imag = res.imag
                print(f"imag (imaginary part) = {round(imag, 12)}")                
            else:
                print('Please enter a valid operation ("i" for info and "<" to exit)')
        except:
            print("OPERATION ERROR") 
            print("This error occurs when the inputs do not meet their restrictions, for example: ")
            print('Only real numbers, constants, and expressions can be entered as terms (enter "i" for info and "<" to exit)')
            print("Division by 0 is undefined")
            print("Raising 0 to a negative power is undefined")
            print()

def from_rectangular():
    global ans
    global real
    global imag
    global ang
    global mod
    print()
    print("Please enter the first term in the form a + bi and the second term (if needed) in the form c + di")               
    while True:
        clear_variables()
        print()
        a = input("a (i for info): ")
        if a == "<" or a == "exit" or a == "exi":
            break
        elif a == "i" or a == "info" or a == "inf":
            print()
            print('Real numbers and expressions, such as "3 * sin(pi / 3)", can be entered as values')
            print("The following non-parenthesized operators and functions can be entered as part of an expression:")
            print("Operators: + (add), - (subtract), * (multiply), / (divide), // (integer divide), % (remainder), ** (exponent)")
            print("Functions: eg. abs(x), sqrt(x), cbrt(x), pow(x, y), log(x, base), factorial(x), comb(x, y), perm(x, y), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), degrees(x), radians(x), sum([x, y, z,...]), int(x), round(x), etc.")
            print('Real constants such as "pi", "e", and "tau" can be entered')
            print('Real variables can also be entered, for example: "ans" (previous real answer), "real" (real part of previous complex result), "imag" (imaginary part of previous complex result), "root" (1st real solution of previous quadratic), "root2" (2nd real solution of previous quadratic), "imag2" (imaginary part of 2nd previous quadratic complex solution) "sum" (previous series summation), "rat" (previous geometric series common ratio), "dif" (previous arithmetic series common difference), "term1" (1st term of previous series), "coef1" (1st coefficient of previous binomial expansion), and stored variables')
            print("The above operators and functions can only be entered as part of an expression, not as an operation")
            print('Enter "p" for polar form, "r" for real operation, "m" for matrix operation, "f" for function (this will direct to polynomial), "s" for summation (this will direct to binomial expansion)')
            print()
            print("Notes:")
            print("Fractional exponents can be used to root: eg. (-1 + 0i) ^ (1/2 + 0i) = i")
            print('Trigonometric functions accept and output angles in radians. The degrees and radians functions or operations can be used to convert')
            print("The result of trigonometric inverse functions (eg. asin, acos, atan, etc.) will lie in their restricted domains")
            print("Integer divide (//) and int() will remove the decimal part from the output, wheras round() will follow the standard rounding rules: eg. 3 // 2 = int(3 / 2) = 1, but round(3 / 2) = 2")
            print("For more information, visit the python math and operators websites")
            continue
        elif a == "p" or a == "polar" or a == "pol" or a == "polar form":
            from_polar()
            break
        elif a == "r" or a == "rea" or a == "real" or a == "real operation":
            real_operation()
            break
        elif a == "f" or a == "fun" or a == "function":
            polynomial()
            break
        elif a == "s" or a == "summation" or a == "sum":
            binomial_expansion()
            break
        elif a == "m" or a == "mat" or a == "matrix":
            matrix_operation()
            break
        try:
            a = eval(a)
        except:
            print('Please enter a real number or expression, "p" for polar form, "r" for real operation, "m" for matrix operation, "f" for function, "s" for summation, "i" got info, or "<" to exit')
            continue
        b = input("b: ")
        if b == "<" or b == "exit" or b == "exi":
            continue
        try:
            b = eval(b)
        except:
            print('Please enter a real number or expression, or "<" to exit')
            continue
        if round(a, 12) != 0 and round(b, 12) > 0:
            if round(b, 12) != 1:
                cterm1 = f"{round(a, 12)} + {round(b, 12)}i"
            else:
                cterm1 = f"{a} + i"
        elif round(a, 12) != 0 and round(b, 12) < 0:
            if round(b, 12) != -1:
                cterm1 = f"{round(a, 12)} - {round(b * -1, 12)}i"
            else:
                cterm1 = f"{round(a, 12)} - i"
        elif round(a, 12) == 0 and round(b, 12) != 0:
            if round(b, 12) != -1 and round(b, 12) != 1:
                cterm1 = f"{round(b, 12)}i"
            elif round(b, 12) == 1:
                cterm1 = "i"
            else:
                cterm1 = "-i"
        elif round(b, 12) == 0:
            cterm1 = f"{round(a, 12)}"
        print("First term: " + cterm1)
        while True:
            print()
            op = input("Operation (i for info): ")
            if op == "info" or op == "i" or op == "inf":
                print()
                print('The following operations can be entered: equals (=), add (+), subtract (-), multiply (*), divide (/), exponent (^), absolute value or modulus (||), angle or argument (ang), polar (pol)')
                print()
                print("Notes:")
                print('The name, sign, or first 3 letters of any operation can be entered: eg. "absolute value", "abs", and "||" all work.')
                print("Fractional exponents can be used to root: eg. (-1 + 0i) ^ (1/2 + 0i) = i.")
                print('Expressions entered as terms can be operated on or evaluated with the "equals" (=) operation.')
                print("The above operations can only be entered as an operation, not as part of an expression.")
            else:
                break
        if op == "<" or op == "exit" or op == "exi":
            continue
        if not(op == "=" or op == "equals" or op == "equ" or op == "argument" or op == "arg" or op == "angle" or op == "ang" or op == "phase" or op == "pha" or op == "polar" or op == "pol" or op == "abs" or op == "absolute value" or op == "magnitude" or op == "mag" or op == "||" or op == "modulus" or op == "mod"):
            print()
            c = input("c: ")
            if c == "<" or c == "exit" or c == "exi":
                continue
            try:
                c = eval(c)
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue                        
            d = input("d: ")
            if d == "<" or d == "exit" or d == "exi":
                continue
            try:
                d = eval(d)
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue
            if round(c, 12) != 0 and round(d, 12) > 0:
                if round(d, 12) != 1:
                    cterm2 = f"{round(c, 12)} + {round(d, 12)}i"
                else:
                    cterm2 = f"{round(c, 12)} + i"
            elif round(c, 12) != 0 and round(d, 12) < 0:
                if round(d, 12) != -1:
                    cterm2 = f"{round(c, 12)} - {round(d * -1, 12)}i"
                else:
                    cterm2 = f"{round(c, 12)} - i"
            elif round(c, 12) == 0 and round(d, 12) != 0:
                if round(d, 12) != 1 and round(d, 12) != -1:
                    cterm2 = f"{round(d, 12)}i"
                elif round(d, 12) == 1:
                    cterm2 = "i"
                else:
                    cterm2 = "-i"
            elif round(d, 12) == 0:
                cterm2 = f"{round(c, 12)}"
            print("Second term: " + cterm2)
        try:
            if op == "=" or op == "equals" or op == "equ":
                res = complex(a, b)
                print()
                print(f"Result: {cterm1}")
                real = res.real
                print(f"real (real part) = {round(real, 12)}")
                imag = res.imag
                print(f"imag (imaginary part) = {round(imag, 12)}")
            elif op == "+" or op == "add":
                res = complex(a, b) + complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                real = res.real
                print(f"real (real part) = {round(real, 12)}")
                imag = res.imag
                print(f"imag (imaginary part) = {round(imag, 12)}")
            elif op == "-" or op == "subtract" or op == "sub":
                res = complex(a, b) - complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                real = res.real
                print(f"real (real part) = {round(real, 12)}")
                imag = res.imag
                print(f"imag (imaginary part) = {round(imag, 12)}")
            elif op == "*" or op == "multiply" or op == "mul":
                res = complex(a, b) * complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                real = res.real
                print(f"real (real part) = {round(real, 12)}")
                imag = res.imag
                print(f"imag (imaginary part) = {round(imag, 12)}")
            elif op == "/" or op == "divide" or op == "div":
                res = complex(a, b) / complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                real = res.real
                print(f"real (real part) = {round(real, 12)}")
                imag = res.imag
                print(f"imag (imaginary part) = {round(imag, 12)}")
            elif op == "^" or op == "exponent" or op == "exp" or op == "**":
                res = complex(a, b) ** complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                real = res.real
                print(f"real (real part) = {round(real, 12)}")
                imag = res.imag
                print(f"imag (imaginary part) = {round(imag, 12)}")
            elif op == "abs" or op == "absolute value" or op == "magnitude" or op == "mag" or op == "||" or op == "modulus" or op == "mod":
                mod = abs(complex(a, b))
                print()
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
            elif op == "angle" or op == "ang" or op == "phase" or op == "pha" or op == "argument" or op == "arg":
                res = cmath.phase(a, b)
                while True:
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "pos" or angle == "+" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(res, 12) < 0:
                                res += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(res, 12) > 0:
                                res -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        res = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(res, 12) < 0:
                                res += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(res, 12) > 0:
                                res -= 360
                        break
                print()                  
                ang = res
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)") 
            elif op == "polar" or op == "pol" or op == "polar form":
                res = cmath.polar(complex(a, b))
                ares = res[1]
                while True:
                    print()
                    unit = input("Output in radians (r) or degrees (d)? ")
                    if not(unit == "r" or unit == "radians" or unit == "rad" or unit == "d" or unit == "degrees" or unit == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output positive (p) or negative (n) angle? ")
                        if not(angle == "positive" or angle == "p" or angle == "+" or angle == "pos" or angle == "-" or angle == "negative" or angle == "n" or angle == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                            print()
                        else:
                            break
                    if unit == "r" or unit == "radians" or unit == "rad":
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit == "d" or unit == "degrees" or unit == "deg":
                        ares = degrees(ares)
                        if angle == "positive" or angle == "p" or angle == "pos" or angle == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle == "negative" or angle == "n" or angle == "neg" or angle == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(abs, 12)}")
                ang = ares
                if unit == "r" or unit == "radians" or unit == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")                    
            else:
                print('Please enter a valid operation ("i" for info and "<" to exit)')
        except:
            print()
            print("OPERATION ERROR") 
            print("This error occurs when the inputs do not meet their restrictions, for example: ")
            print('Only real numbers, constants, and expressions can be entered as terms (enter "i" for info and "<" to exit)')
            print("Division by 0 is undefined")
            print("Raising 0 to a negative power is undefined")
            print()

def real_operation():
    global ans
    print()
    print("Please enter the first real operation term")
    while True:
        clear_variables()
        print()
        n = input('First term (i for info): ')
        if n == "exit" or n == "<" or n == "exi":
            break
        elif n == "i" or n == "inf" or n == "info":
            print()
            print('Real numbers and expressions, such as "3 * sin(pi / 3)", can be entered as terms.')
            print("The following non-parenthesized operators and functions can be entered as part of an expression:")
            print("Operators: + (add), - (subtract), * (multiply), / (divide), // (integer divide), % (remainder), ** (exponent)")
            print("Functions: eg. abs(x), sqrt(x), cbrt(x), pow(x, y), log(x, base), factorial(x), comb(x, y), perm(x, y), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), degrees(x), radians(x), sum([x, y, z,...]), int(x), round(x), etc.")
            print('Real constants such as "pi", "e", and "tau" can be entered.')
            print('Real variables can also be entered, for example: "ans" (previous real answer), "real" (real part of previous complex result), "imag" (imaginary part of previous complex result), "root" (1st real solution of previous quadratic), "root2" (2nd real solution of previous quadratic), "imag2" (imaginary part of 2nd previous quadratic complex solution) "sum" (previous series summation), "rat" (previous geometric series common ratio), "dif" (previous arithmetic series common difference), "term1" (1st term of previous series), "coef1" (1st coefficient of previous binomial expansion), and stored variables')
            print("The above operators and functions can only be entered as part of an expression, not as an operation.")
            print('Enter "c" for complex operation (this will direct to rectangular form), "m" for matrix operation, "f" for function (this will direct to polynomial), and "s" for summation (this will direct to binomial expansion)')
            print()
            print("Notes:")
            print("Fractional exponents can be used to root: eg. 8 ^ (1/3) = 2.")
            print('Trigonometric functions accept and output angles in radians. The degrees and radians functions or operations can be used to convert.')
            print("The result of trigonometric inverse functions (eg. asin, acos, atan, etc.) will lie in their restricted domains.")
            print("Integer divide (//) and int() will remove the decimal part from the output, wheras round() will follow the standard rounding rules: eg. 3 // 2 = int(3 / 2) = 1, but round(3 / 2) = 2.")
            print("For more information, visit the python math and operators websites.")
            continue
        elif n == "c" or n == "com" or n == "complex" or n == "complex operation":
            from_rectangular()
            break
        elif n == "s" or n == "sum" or n == "summation":
            binomial_expansion()
            break
        elif n == "f" or n == "fun" or n == "function":
            polynomial()
            break
        elif n == "m" or n == "mat" or n == "matrix" or n == "matric operation":
            matrix_operation()
            break
        else:
            try:
                n = eval(n)
            except:
                print('Please enter a real number or expression, "c" for complex operation, "m" for matrix operation, "f" for function, "s" for summation, "i" for info, or "<" to exit')
                continue
            while True:
                op = input('Operation (i for info): ')
                if op == "info" or op == "i" or op == "inf":
                    print()
                    print("The following operations can be entered:")
                    print('Basic: add (+), subtract (-), multiply (*), divide (/), integer divide or floor divide (//), remainder or modulo (r or %), absolute value or magnitude (||)')
                    print('Power: exponent (^), logarithm (log), square root (sqrt), cube root (cbrt)')
                    print('Trigonometry: sine (sin), cosine (cos), tangent (tan), arcsine (asin), arccosine (acos), arctangent (atan), degrees (deg), radians (rad)')
                    print("Combinatorics: factorial (!), choose (cho), permute (per)")
                    print("Other: equals (=), store (sto), round (~), integer (int)")
                    print()
                    print("Notes:")
                    print('The name, sign, or first 3 letters of any operation can be entered: eg. "factorial", "fac", and "!" all work.')
                    print("Fractional exponents can be used to root: eg. 8 ^ (1/3) = 2.")
                    print('The "integer divide" (//) and "integer" (int) operations will remove the decimal part from the output, wheras the "round" (~) operation will follow the standard rounding rules: eg. 3 // 2 = int(3 / 2) = 1, but round(3 / 2) = 2.')
                    print('The variable name for the "store" (sto) operation must begin with a capital letter')
                    print('Expressions entered as terms can be operated on or evaluated with the "equals" (=) operation.')
                    print("The above operations can only be entered as an operation, not as part of an expression.")
                    print()
                else:
                    break
            if op == "exit" or op == "<":
                continue
            elif not(op == "store" or op == "sto" or op == "equals" or op == "=" or op == "equ" or op == "==" or op == "factorial" or op == "fac" or op == "!" or op == "sqrt" or op == "square root" or op == "squ" or op == "cbrt" or op == "cube root" or op == "cub" or op == "absolute value" or op == "||" or op == "abs" or op == "magnitude" or op == "mag" or op == "asin" or op == "arcsine" or op == "inverse sine" or op == "inv sin" or op == "acos" or op == "arccosine" or op == "inverse cosine" or op == "inv cos" or op == "atan" or op == "arctangent" or op == "inverse tangent" or op == "inv tan" or op == "asi" or op == "aco" or op == "ata" or op == "sin" or op == "sine" or op == "cos" or op == "cosine" or op == "tangent" or op == "tan" or op == "int" or op == "integer" or op == "radians" or op == "rad" or op == "degrees" or op == "deg"):
                if op == "exponent" or op == "^" or op == "exp" or op == "**":
                    n2 = input('Exponent: ')
                    if n2 == "<" or n2 == "exit" or n2 == "exi":
                        continue
                    try:
                        n2 = eval(n2)
                    except:
                        print('Please enter a real number or expression, or "<" to exit')
                        continue
                elif op == "round" or op == "~" or op == "rou":
                    n2 = input('Decimals to round (0-12): ')
                    if n2 == "ans":
                        n2 = ans
                    elif n2 == "<" or n2 == "exit" or n2 == "exi":
                        continue
                    try:
                        n2 = int(n2)
                    except:
                        print('Please enter an integer from 0 to 12 or "<" to exit')
                        continue
                elif op == "log" or op == "logarithm":
                    if n > 0:
                        n2 = input('Base: ')
                        if n2 == "<" or n2 == "exit" or n2 == "exi":
                            continue
                        try:
                            n2 = eval(n2)
                        except:
                            print('Please enter a real number or expression greater than 0 and not equal to 1, or "<" to exit')
                            continue                                
                elif op == "choose" or op == "cho" or op == "comb":
                    if round(n, 12) == round(n) and n >= 0:
                        n2 = input(f'From {round(n)} choose: ')
                        if n2 == "<" or n2 == "exit" or n2 == "exi":
                            continue
                        try:
                            n2 = eval(n2)
                        except:
                            print('Please enter a nonnegative integer or "<" to exit')
                            continue                                    
                elif op == "perm" or op == "permute" or op == "per":
                    if round(n, 12) == round(n) and n >= 0:
                        n2 = input(f'From {round(n)} permute: ')
                        if n2 == "<" or n2 == "exit" or n2 == "exi":
                            continue
                        try:
                            n2 = eval(n2)
                        except:
                            print('Please enter a nonnegative integer or "<" to exit')
                            continue  
                else:
                    n2 = input('Next term: ')
                    if n2 == "<" or n2 == "exit" or n2 == "exi":
                        continue
                    try:
                        n2 = eval(n2)
                    except:
                        print('Please enter a real number or expression, or "<" to exit')
                        continue
        try:
            if op == "equals" or op == "=" or op == "equ" or op == "==":
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "add" or op == "+":
                n += n2
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "subtract" or op == "-" or op == "sub":
                n -= n2
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "multiply" or op == "*" or op == "mul":
                n *= n2
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "divide" or op == "/" or op == "div":
                n /= n2
                if n == 0:
                    n = 0.0
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "remainder" or op == "r" or op == "%" or op == "modulo" or op == "rem" or op == "mod":
                n %= n2
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "exponent" or op == "^" or op == "exp" or op == "**":
                n **= n2
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "store" or op == "sto":
                while True:
                    vname = input("Variable name (i for info): ")
                    if vname == "<" or vname == "exit" or vname == "exi":
                        break
                    try:
                        if vname[0].isalpha() == False or vname[0].islower():
                            print("Please enter a variable name beginning with a capital letter")
                            print()
                        else:
                            break
                    except:
                        print("Please enter a variable name beginning with a capital letter")
                        print()
                if vname == "<" or vname == "exit" or vname == "exi":
                    continue
                globals()[vname] = n
                print()
                print(vname + f" = {round(n, 12)}")
                keeps.append(vname)
            elif op == "round" or op == "~" or op == "rou":
                if n2 > 12:
                    n2 = 12
                n = round(n, n2)
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "factorial" or op == "!" or op == "fac":
                n = factorial(round(n))
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "sqrt" or op == "square root" or op == "squ":
                n = sqrt(n)
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "cbrt" or op == "cube root" or op == "cub":
                n = cbrt(n)
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "log" or op == "logarithm":
                n = log(n, n2)
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "integer divide" or op == "int div" or op == "floor divide" or op == "flo div" or op == "//":
                n //= n2
                print()
                if n == 0:
                    n = 0.0
                print(f"ans = {round(n, 12)}")
            elif op == "integer" or op == "int":
                n = int(n)
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "choose" or op == "cho" or op == "comb":
                n = comb(round(n), round(n2))
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "perm" or op == "permute" or op == "per":
                n = perm(round(n), round(n2))
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "absolute value" or op == "||" or op == "abs" or op == "magnitude" or op == "mag":
                n = abs(n)
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "radians" or op == "rad":
                n = radians(n)
                print()
                print(f"ans = {round(n, 12)}")
            elif op == "degrees" or op == "deg":
                n = degrees(n)
                print()
                print(f"ans = {round(n, 12)}")             
            elif op == "sin" or op == "sine" or op == "cos" or op == "cosine" or op == "tangent" or op == "tan":
                angle = input("Inputted in radians (r) or degrees (d)? ")
                if angle == "radians" or angle == "rad" or angle == "r":
                    n = n
                    go = True
                elif angle == "degrees" or angle == "deg" or angle == "d":
                    n = radians(n)
                    go = True
                else:
                    print('Please enter either "r" for radians or "d" for degrees')
                    go = False
                if go == True:
                    if op == "sin" or op == "sine":
                        n = sin(n)
                        print()
                        print(f"ans = {round(n, 12)}")
                    elif op == "cos" or op == "cosine":
                        n = cos(n)
                        print()
                        print(f"ans = {round(n, 12)}")
                    elif op == "tan" or op == "tangent":
                        n = tan()
                        print()
                        print(f"ans = {round(n, 12)}")
            elif op == "asin" or op == "arcsine" or op == "inverse sine" or op == "inv sin" or op == "acos" or op == "arccosine" or op == "inverse cosine" or op == "inv cos" or op == "atan" or op == "arctangent" or op == "inverse tangent" or op == "inv tan" or op == "asi" or op == "aco" or op == "ata":
                unit = input("Output in radians (r) or degrees (d)? ")
                quad = input("Output in default quadrant (yes/no)? ")
                go = True
                if op == "asin" or op == "asi" or op == "arcsine" or op == "inverse sine" or op == "inv sin":
                    if quad == "yes" or quad == "y":
                        if unit == "radians" or unit == "rad" or unit == "r":
                            n = asin(n)
                        elif unit == "degrees" or unit == "deg" or unit == "d":
                            n = degrees(asin(n))                              
                    elif quad == "no" or quad == "n":
                        if unit == "radians" or unit == "rad" or unit == "r":
                            n = pi - asin(n)
                        elif unit == "degrees" or unit == "deg" or unit == "d":
                            n = 180 - degrees(asin(n))                           
                elif op == "acos" or op == "arccosine" or op == "aco" or op == "inverse cosine" or op == "inv cos":
                    if quad == "yes" or quad == "y":
                        if unit == "radians" or unit == "rad" or unit == "r":
                            n = acos(n)
                        elif unit == "degrees" or unit == "deg" or unit == "d":
                            n = degrees(acos(n))
                    elif quad == "no" or quad == "n":
                        if unit == "radians" or unit == "rad" or unit == "r":
                            n = -acos(n)
                        elif unit == "degrees" or unit == "deg" or unit == "d":
                            n = -degrees(acos(n))
                elif op == "atan" or op == "arctangent" or op == "ata" or op == "inverse tangent" or op == "inv tan":
                    if quad == "yes" or quad == "y":
                        if unit == "radians" or unit == "rad" or unit == "r":
                            n = atan(n)
                        elif unit == "degrees" or unit == "deg" or unit == "d":
                            n = degrees(atan(n))
                    elif quad == "no" or quad == "n":
                        if unit == "radians" or unit == "rad" or unit == "r":
                            n = pi - atan(n)
                        elif unit == "degrees" or unit == "deg" or unit == "d":                            
                            n = 180 - degrees(atan(n))
                angle = input("Output positive (p) or negative (n) angle? ")
                if angle == "positive" or angle == "pos" or angle == "+" or angle == "p":
                    if unit == "radians" or unit == "rad" or unit == "r":
                        if round(n, 12) < 0:
                            n += 2 * pi
                    elif unit == "degrees" or unit == "deg" or unit == "d":
                        if round(n, 12) < 0:
                            n += 360
                    else:
                        go = False
                elif angle == "negative" or angle == "neg" or angle == "-" or angle == "n":
                    if unit == "radians" or unit == "rad" or unit == "r":
                        if round(n, 12) > 0:
                            n -= 2 * pi
                    elif unit == "degrees" or unit == "deg" or unit == "d":
                        if round(n, 12) > 0:
                            n -= 360
                    else:
                        go = False
                if unit != "radians" and unit != "rad" and unit != "r" and unit != "d" and unit != "degrees" and unit != "deg":
                    print()
                    print('Please enter either "r" for radians or "d" for degrees')
                    go = False
                if quad != "yes" and quad != "y" and quad != "no" and quad != "n":
                    print('Please enter either "yes" (y) or "no" (n)')
                    go = False       
                if angle != "p" and angle != "n" and angle != "positive" and angle != "negative" and angle != "pos" and angle != "+" and angle != "-" and angle != "neg":
                    print('Please enter either "p" for positive or "n" for negative')
                    print()
                    go = False
                if go == True:
                    print()
                    if unit == "radians" or unit == "rad" or unit == "r":
                        print(f"ans = {round(n, 12)} radians")
                    else:
                        print(f"ans = {round(n, 12)} degrees")
            else:
                print('Please enter a valid operation ("i" for info and "<" to exit)')
                print()
                continue
            ans = n
        except:
            print()
            print("OPERATION ERROR") 
            print("This error occurs when the inputs do not meet their restrictions, for example: ")
            print('Only real numbers, constants, and expressions can be entered as terms (enter "i" for info and "<" to exit)')
            print("Division, integer division, and remainder/modulo by 0 is undefined")
            print("Raising 0 to a negative power is undefined")
            print("Taking an even root of a negative number is undefined over real numbers")
            print("The factorial, choose, and permute functions only accepts nonnegative integers")
            print("The logarithm function only accepts positive arguments and positive bases not equal to 1")
            print()

def binomial_expansion():
    global binsum
    print()
    print("Please enter the binomial in the form (ax^b + cy^d) ^ n, where x and y are non-numeric variable names without spaces, a, b, and c are not equal to 0, and n is an integer")
    while True:
        clear_variables()
        binsum = ""
        print()
        a = input("a (i for info): ")
        if a == "<" or a == "exit" or a == "exi":
            break
        elif a == "o" or a == "ope" or a == "operation":
            real_operation()
            break
        elif a  == "a" or a == "ari" or a == "arithmetic" or a == "arithmetic series":
            arithmetic()
            break
        elif a  == "g" or a == "geo" or a == "geometric" or a == "geometric series":
            geometric()
            break
        elif a == "f" or a == "fun" or a == "function":
            polynomial()
            break
        elif a == "i" or a == "info" or a == "inf":
            print('Please enter a nonzero real number or expression as the first coefficient')
            print('Enter "a" for arithmetic series, "g" for geometric series, "o" for operation (this will direct to real operation), and "f" for function (this will direct to polynomial)')
            continue
        try:
            a = eval(a)
        except:
            print('Please enter a nonzero real number or expression, "a" for arithmetic series, "g" for geometric series, "o" for operation, "f" for function, "i" for info, or "<" to exit')
            continue
        if a == 0:
            print('Please enter a nonzero real number or expression, "a" for arithmetic series, "g" for geometric series, "o" for operation, "f" for function, "i" for info, or "<" to exit')
            continue
        while True:
            x = input("x (i for info): ")
            if x == "exit" or x == "exi" or x == "<":
                break
            try:
                if x == "info" or x == "inf" or x == "i":
                    print()
                    print("Please enter a non-numeric variable name without spaces")
                    print("The variable will not store any value, it is just the name that will be printed in the result")
                    print()
                elif x.find(" ") != -1 or x[0].isalpha() == False:
                    print('For clarity, please enter a non-numeric variable name without spaces, "i" for info, or "<" to exit')
                    print()
                else:
                    break
            except:
                print('Please enter a non-numeric variable name without spaces, "i" for info, or "<" to exit')
        if x == "exit" or x == "exi" or x == "<":
            continue
        b = input("b: ")
        if b == "<" or b == "exit" or b == "exi":
            continue
        try:
            b = eval(b)
        except:
            print('Please enter a nonzero real number or expression, or "<" to exit')
            continue
        if b == 0:
            print('Please enter a nonzero real number or expression, or "<" to exit')
            continue
        c = input("c: ")
        if c == "<" or c == "exit" or c == "exi":
            continue
        try:
            c = eval(c)
        except:
            print('Please enter a nonzero real number or expression, or "<" to exit')
            continue
        if c == 0:
            print('Please enter a nonzero real number or expression, or "<" to exit')
            continue
        while True:
            y = input("y (i for info, > to skip): ")
            if y == "exit" or y == "exi" or y == "<":
                break
            try:
                if y == "info" or y == "inf" or y == "i":
                    print()
                    print("Please enter a non-numeric variable name without spaces")
                    print("The variable will not store any value, it is just the name that will be printed in the result")
                    print("Skipping will is equivalent to setting the variable's exponent to 0")
                    print()
                elif y == "skip" or y == ">" or y == "ski":
                    break
                elif y.find(" ") != -1 or y[0].isalpha() == False:
                    print('For clarity, please enter a non-numeric variable name without spaces, "i" for info, or "<" to exit')
                    print()
                else:
                    break
            except:
                print('Please enter a non-numeric variable name without spaces, "i" for info, or "<" to exit')
                print()
        if y == "exit" or y == "exi" or y == "<":
            continue
        if y != "skip" and y != "ski" and y != ">":
            d = input("d: ")
            if d == "<" or d == "exit" or d == "exi":
                continue
            try:
                d = eval(d)
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue
        else:
            d = 0
        n = input("n: ")
        if n == "<" or n == "exit" or n == "exi":
            continue
        try:
            n = int(n)
            if n < 0:
                binsum += "1 / ("
        except:
            print('Please enter an integer or "<" to exit')
            continue
        while True:
            print()
            un = input(f"Index of terms to find/sum (1-{abs(n)+1} for all, i for info): ")
            if un == "i" or un == "info" or un == "inf":
                print()
                print("Please enter a list of exponents seperated by commas and using dashes to indicate ranges:")
                print('eg. "1, 3, 6-8, 10" will output the 1st, 3rd, 6th, 7th, 8th, and 10th terms, given that n >= 9.')
                if n >= 0:
                    print("If n is negative (it's not!), only the denominator of each term will be outputted (the sum will still be complete)")
                else:
                    print("If n is negative (it is!), only the denominator of each term will be outputted (the sum will still be complete)")
                print(f"All indexes must be positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive, and the second index of a range must be greater than the first index of the range.")
                print()
            else:
                break
        if un == "<" or un == "exit" or un  == "exi":
            continue
        if un == "all":
            un = f"1-{abs(n)+1}"
        un = un.split(",")
        print()
        unindex = 0
        while unindex < len(un):
            rangelist = un[unindex].split("-")
            if len(rangelist) == 1:
                try:
                    unterm = un[unindex]
                    if unterm == "ans":
                        unterm = ans
                    unterm = int(unterm)
                    if 0 < unterm <= abs(n) + 1:
                        k = unterm - 1
                        print_binomial(a, b, c, d, n, k, unterm, x, y)
                        binsum = binsum[:len(binsum) - 3]
                        if n < 0:
                            binsum += ")"
                        print("Sum: " + binsum)
                    else:
                        print(f'Term Error: indexes must be positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive (enter "all" for all, "i" for info and "<" to exit)')
                except:
                    print(f'Term Error: indexes must be positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive (enter "all" for all, "i" for info and "<" to exit)')
            elif len(rangelist) == 2:
                try:
                    if rangelist[0] == "ans":
                        rangelist[0] = ans
                    if rangelist[1] == "ans":
                        rangelist[1] = ans
                    rangelist[0] = int(rangelist[0])
                    rangelist[1] = int(rangelist[1])
                    if rangelist[0] > 0 and rangelist[1] > rangelist[0] and rangelist[1] <= abs(n) + 1:
                        rangelist = list(range(rangelist[0], rangelist[1] + 1))
                        rangeindex = 0
                        while rangeindex < len(rangelist):
                            unterm = rangelist[rangeindex]
                            k = unterm - 1
                            print_binomial(a, b, c, d, n, k, unterm, x, y)
                            rangeindex += 1
                        binsum = binsum[:len(binsum) - 3]
                        if n < 0:
                            binsum += ")"
                        print("Sum: " + binsum)
                    elif rangelist[1] <= rangelist[0]:
                        print('Term Error: the second index of a range must be greater than the first index of the range (enter "all" for all, "i" for info and "<" to exit)')
                    else:    
                        print(f'Term Error: indexes must be positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive (enter "all" for all, "i" for info and "<" to exit)')
                except:
                    print(f'Term Error: indexes must be positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive (enter "all" for all, "i" for info and "<" to exit)')
            else:
                print(f'Term Error: please enter ranges in the form "x-y", where x and y are both positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive, and y is greater than x (enter "all" for all, "i" for info and "<" to exit)')
            unindex += 1

def arithmetic():
    global dif
    global sum
    global index
    print()
    print("Please enter one of the arithmetic series terms and its index")
    while True:
        clear_variables()
        print()
        b = input("Term (i for info): ")
        if b == "<" or b == "exit" or b == "exi":
            break
        elif b == "o" or b == "ope" or b == "operation":
            real_operation()
            break
        elif b == "g" or b == "geo" or b == "geometric" or b == "geometric series":
            geometric()
            break
        elif b == "b" or b == "bin" or b == "binomial" or b == "binomial expansion":
            binomial_expansion()
            break
        elif b == "f" or b == "fun" or b == "function":
            polynomial()
            break
        elif b == "i" or b == "info" or b == "inf":
            print("Please enter a real number or expression as the value of one of the series terms")
            print('Enter "b" for binomial expansion, "g" for geometric series, "o" for operation (this will direct to real operation), and "f" for function (this will direct to polynomial)')
            continue
        try:
            b = eval(b)
        except:
            print('Please enter a real number or expression, "b" for binomial expansion, "g" for geometric series, "o" for operation, "f" for function, "i" for info, or "<" to exit')
            continue
        bn = input("Term index: ")
        if bn == "<" or bn == "exit" or bn == "exi":
            continue     
        elif bn == "ans":
            bn = ans
        try:
            bn = int(bn)
        except:
            print('Please enter a positive integer or "<" to exit')
            continue
        if bn < 1:
            print('Please enter a positive integer or "<" to exit')
            continue
        print()
        atype = input("Enter common difference (d) or another term (t)? ")
        if atype == "t" or atype == "term" or atype == "ter" or atype == "another term" or atype == "ano ter":
            c = input("Next term: ")
            if c == "<" or c == "exit" or c == "exi":
                continue
            try:
                c = eval(c)  
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue
            cn = input("Term index: ")
            if cn == "<" or cn == "exit" or cn == "exi":
                continue     
            elif cn == "ans":
                cn = ans
            try:
                cn = int(cn)
            except:
                print('Please enter a positive integer or "<" to exit')
                continue
            if bn < cn:
                comdif = (c - b) / (cn - bn)
            else:
                print("The index of term 2 must be greater than the index of term 1")
                continue
            a = b - comdif * (bn - 1)
        elif atype == "common difference" or atype == "dif" or atype == "d" or atype == "difference" or atype == "com dif":
            comdif = input("Common difference: ")
            if comdif == "<" or comdif == "exit" or comdif == "exi":
                continue
            try:
                comdif = eval(comdif)
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue
            cn = bn + 1
            c = b + comdif
            a = b - comdif * (bn - 1)
        elif atype == "<" or atype == "exit" or atype == "exi":
            continue
        else:
            print('Please enter either "d" for difference, "t" for term, or "<" to exit')
            continue
        print()
        if comdif != 0:
            asumtype = input("Enter number of terms to sum (n) or last term (l) (> to skip)? ")
        else:
            asumtype = "n"
        if asumtype == "n" or asumtype == "number of terms to sum" or asumtype == "num" or asumtype == "number":
            if comdif != 0:
                n = input("Number of terms: ")
            else:
                n = input("Number of terms to sum (> to skip): ")
            if comdif != 0 or (n != ">" and n != "skip" and n != "ski"):
                if n == "<" or n == "exit" or n == "exi":
                    continue     
                elif n == "ans":
                    n = ans
                try:
                    n = int(n)
                except:
                    print('Please enter a positive integer or "<" to exit')
                    continue
                if n <= 0:
                    print('Please enter a positive integer or "<" to exit')
                    continue
        elif asumtype == "l" or asumtype == "las" or asumtype == "last" or asumtype == "last term" or asumtype == "las ter":
            l = input("Last term: ")
            if l == "<" or l == "exit" or l == "exi":
                continue
            try:
                l = eval(l)
            except:
                print('Please enter a real number or expression, or "<" to exit')
                continue
            if l == a:
                print("If the common difference is 0, enter a number of terms to sum instead")
                continue
            n = (l - a) / comdif + 1
            if round(n) != round (n, 12) or n <= 0:
                print("The entered term is not a term of the series: please enter different terms")
                continue
        elif not(asumtype == ">" or asumtype == "skip" or asumtype == "ski"):
            print('Please enter "n" for number of terms to sum, "l" for last term, or ">" to skip')
            continue
        while True:
            un = input('Index of terms to find (i for info, > to skip): ')
            if un == "i" or un == "info" or un == "inf":
                print()
                print("Please enter a list of indexes seperated by commas and using dashes to indicate ranges:")
                print('eg. "1, 3, 6-8, 10" will output the 1st, 3rd, 6th, 7th, 8th, and 10th terms.')
                print("All indexes must be positive integers, and the second index of a range must be greater than the first index of the range.")
                print()
            else:
                break
        if un == "<" or un == "exit" or un == "exi":
            continue
        elif un != ">" and un != "skip" and un != "ski":
            un = un.split(",")
            print()
            unindex = 0
            while unindex < len(un):
                rangelist = un[unindex].split("-")
                if len(rangelist) == 1:
                    try:
                        unterm = un[unindex]
                        if unterm == "ans":
                            unterm = ans
                        unterm = int(unterm)
                        if unterm > 0:
                            sumterm = f"term{unterm}"
                            globals()[sumterm] = a + comdif * (unterm - 1)
                            keeps.append(sumterm)
                            print(sumterm + f" (term {unterm}) = {round(a + comdif * (unterm - 1), 12)}")
                        else:
                            print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                    except:
                        print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                elif len(rangelist) == 2:
                    try:
                        if rangelist[0] == "ans":
                            rangelist[0] = ans
                        if rangelist[1] == "ans":
                            rangelist[1] = ans
                        rangelist[0] = int(rangelist[0])
                        rangelist[1] = int(rangelist[1])
                        if rangelist[0] > 0 and rangelist[1] > rangelist[0]:
                            rangelist = list(range(rangelist[0], rangelist[1] + 1))
                            rangeindex = 0
                            while rangeindex < len(rangelist):
                                unterm = rangelist[rangeindex]
                                sumterm = f"term{unterm}"
                                globals()[sumterm] = a + comdif * (unterm - 1)
                                keeps.append(sumterm)
                                print(sumterm + f" (term {unterm}) = {round(a + comdif * (unterm - 1), 12)}")
                                rangeindex += 1
                        elif rangelist[1] <= rangelist[0]:
                            print('Term Error: the second index of a range must be greater than the first index of the range (enter "i" for info, ">" to skip, and "<" to exit)')
                        else:    
                            print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                    except:
                        print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                else:
                    print('Term Error: please enter ranges in the form "x-y", where x and y are both positive integers and y is greater than x (enter "i" for info, ">" to skip, and "<" to exit)')
                unindex += 1
        else:
            print()
        if asumtype == "l" or asumtype == "las" or asumtype == "last" or asumtype == "last term" or asumtype == "las ter":
            index = n
            print(f"index (of last term) = {round(index, 12)}")
        dif = comdif
        print(f"dif (common difference) = {round(dif, 12)}")
        if n != ">" and n != "skip" and n != "ski" and asumtype != "skip" and asumtype != ">" and asumtype != "ski":
            sum = (2 * a + comdif * (n - 1)) * n / 2
            if round(sum, 12) == 0:
                sum = 0.0
            print(f"sum = {round(sum, 12)}")

def geometric():
    global rat
    global sum
    global index
    print()
    print("Please enter one of the geometric series terms and its index")
    while True:
        clear_variables()
        print()
        b = input("Term (i for info): ")
        if b == "<" or b == "exit" or b == "exi":
            break
        elif b == "o" or b == "ope" or b == "operation":
            real_operation()
            break
        elif b == "a" or b == "ari" or b == "arithmetic" or b == "arithmetic series":
            arithmetic()
            break
        elif b == "b" or b == "bin" or b == "binomial" or b == "binomial expansion":
            binomial_expansion()
            break
        elif b == "f" or b == "fun" or b == "function":
            polynomial()
            break
        elif b == "i" or b == "info" or b == "inf":
            print("Please enter a real number or expression as the value of one of the series terms")
            print('Enter "b" for binomial expansion, "a" for arithmetic series, "o" for operation (this will direct to real operation), and "f" for function (this will direct to polynomial)')
            continue
        try:
            b = eval(b)
        except:
            print('Please enter a nonzero real number or expression, "b" for binomial expansion, "a" for arithmetic series, "o" for operation, "f" for function, "i" for info, or "<" to exit')
            continue
        if round(b, 12) == 0:
            print('Please enter a nonzero real number or expression, "b" for binomial expansion, "a" for arithmetic series, "o" for operation, "f" for function, "i" for info, or "<" to exit')
            continue
        bn = input("Term index: ")
        if bn == "<" or bn == "exit" or bn == "exi":
            continue     
        elif bn == "ans":
            bn = ans
        try:
            bn = int(bn)
        except:
            print('Please enter a positive integer or "<" to exit')
            continue
        if bn < 1:
            print('Please enter a positive integer or "<" to exit')
            continue
        print()
        gtype = input("Enter common ratio (r) or another term (t)? ")
        if gtype == "t" or gtype == "term" or gtype == "ter" or gtype == "another term" or gtype == "ano ter":
            c = input("Next term: ")
            if c == "<" or c == "exit" or c == "exi":
                continue
            try:
                c = eval(c)  
            except:
                print('Please enter a nonzero real number or expression, or "<" to exit')
                continue      
            if round(c, 12) == 0:
                print('Please enter a nonzero real number or expression, or "<" to exit')
                continue
            cn = input("Term index: ")
            if cn == "<" or cn == "exit" or cn == "exi":
                continue     
            elif cn == "ans":
                cn = ans
            try:
                cn = int(cn)
            except:
                print('Please enter a positive integer or "<" to exit')
                continue
            if bn < cn:
                comrat = (c / b) ** (1/(cn - bn))
                if (cn - bn) % 2 == 0:
                    ratsign = input("Use positive (p) or negative (n) common ratio? ")
                    if ratsign == "negative" or ratsign == "neg" or ratsign == "n" or ratsign == "-":
                        comrat *= -1
                    elif ratsign != "positive" and ratsign != "pos" and ratsign != "p" and ratsign != "+":
                        print('Please enter either "p" for positive or "n" for negative')
            else:
                print("The index of term 2 must be greater than the index of term 1")
                continue
            a = b / comrat ** (bn - 1)
        elif gtype == "common ratio" or gtype == "rat" or gtype == "r" or gtype == "ratio" or gtype == "com rat":
            comrat = input("Common ratio: ")
            if comrat == "<" or comrat == "exit" or comrat == "exi":
                continue
            try:
                comrat = eval(comrat)
            except:
                print('Please enter a nonzero real number or expression, or "<" to exit')
                continue
            if round(comrat, 12) == 0:
                print('Please enter a nonzero real number or expression, or "<" to exit')
                continue
            cn = bn + 1
            c = b * comrat
            a = b / comrat ** (bn - 1)
        elif gtype == "<" or gtype == "exit" or gtype == "exi":
            continue
        else:
            print('Please enter either "r" for ratio, "t" for term, or "<" to exit')
            continue
        print()
        if comrat != 1:
            gsumtype = input("Enter number of terms to sum (n) or last term (l) (> to skip)? ")
        else:
            gsumtype = "n"
        if gsumtype == "n" or gsumtype == "number of terms to sum" or gsumtype == "num" or gsumtype == "number":
            if comrat != 1:
                n = input("Number of terms (inf for infinity): ")
            else:
                n = input("Number of terms to sum (inf for infinity, > to skip): ")
            if comrat != 1 or (n != ">" and n != "skip" and n != "ski"):
                if n == "<" or n == "exit" or n == "exi":
                    continue     
                elif n == "ans":
                    n = ans
                elif n != "infinity" and n != "inf":
                    try:
                        n = int(n)
                    except:
                        print('Please enter a positive integer, "inf" for infinity, ">" to skip, or "<" to exit')
                        continue
                    if n <= 0:
                        print('Please enter a positive integer, "inf" for infinity, ">" to skip, or "<" to exit')
                        continue
                elif (n == "inf" or n == "infinity") and (comrat >= 1 or comrat <= -1):
                    print("Infinity is only accepted for common ratios between -1 and 0 and between 0 and -1")
                    continue
        elif gsumtype == "l" or gsumtype == "las" or gsumtype == "last" or gsumtype == "last term" or gsumtype == "las ter":
            l = input("Last term: ")
            if l == "<" or l == "exit" or l == "exi":
                continue
            try:
                l = eval(l)
            except:
                print('Please enter a nonzero real number or expression, or "<" to exit')
                continue
            if l == 0:
                print("The last term cannot be 0")
                continue
            if l == a:
                print("If the common ratio is 1, enter a number of terms to sum instead")
                continue
            n = log(abs(l / a), abs(comrat)) + 1
            if round(n) != round (n, 12) or n <= 0:
                print("The entered term is not a term of the series: please enter different terms")
                continue
        elif not(gsumtype == ">" or gsumtype == "skip" or gsumtype == "ski"):
            print('Please enter "n" for number of terms to sum, "l" for last term, or ">" to skip')
            continue
        while True:
            un = input('Index of terms to find (i for info, > to skip): ')
            if un == "i" or un == "info" or un == "inf":
                print()
                print("Please enter a list of indexes seperated by commas and using dashes to indicate ranges:")
                print('eg. "1, 3, 6-8, 10" will output the 1st, 3rd, 6th, 7th, 8th, and 10th terms.')
                print("All indexes must be positive integers, and the second index of a range must be greater than the first index of the range.")
                print()
            else:
                break
        if un == "<" or un == "exit" or un == "exi":
            continue
        elif un != ">" and un != "skip" and un != "ski":
            un = un.split(",")
            print()
            unindex = 0
            while unindex < len(un):
                rangelist = un[unindex].split("-")
                if len(rangelist) == 1:
                    try:
                        unterm = un[unindex]
                        if unterm == "ans":
                            unterm = ans
                        unterm = int(unterm)
                        if unterm > 0:
                            sumterm = f"term{unterm}"
                            globals()[sumterm] = a * comrat ** (unterm - 1)
                            keeps.append(sumterm)
                            print(sumterm + f" (term {unterm}) = {round(a * comrat ** (unterm - 1), 12)}")
                        else:
                            print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                    except:
                        print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                elif len(rangelist) == 2:
                    try:
                        if rangelist[0] == "ans":
                            rangelist[0] = ans
                        if rangelist[1] == "ans":
                            rangelist[1] = ans
                        rangelist[0] = int(rangelist[0])
                        rangelist[1] = int(rangelist[1])
                        if rangelist[0] > 0 and rangelist[1] > rangelist[0]:
                            rangelist = list(range(rangelist[0], rangelist[1] + 1))
                            rangeindex = 0
                            while rangeindex < len(rangelist):
                                unterm = rangelist[rangeindex]
                                sumterm = f"term{unterm}"
                                globals()[sumterm] = a * comrat ** (unterm - 1)
                                keeps.append(sumterm)
                                print(sumterm + f" (term {unterm}) = {round(a * comrat ** (unterm - 1), 12)}")
                                rangeindex += 1
                        elif rangelist[1] <= rangelist[0]:
                            print('Term Error: the second index of a range must be greater than the first index of the range (enter "i" for info, ">" to skip, and "<" to exit)')
                        else:    
                            print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                    except:
                        print('Term Error: indexes must be positive integers (enter "i" for info, ">" to skip, and "<" to exit)')
                else:
                    print('Term Error: please enter ranges in the form "x-y", where x and y are both positive integers and y is greater than x (enter "i" for info, ">" to skip, and "<" to exit)')
                unindex += 1
        else:
            print()
        if gsumtype == "l" or gsumtype == "las" or gsumtype == "last" or gsumtype == "last term" or gsumtype == "las ter":
            index = n
            print(f"index (of last term) = {round(index, 12)}")
        if round(b, 12) != round(c, 12):
            rat = comrat
            print(f"rat (common ratio) = {round(rat, 12)}")
            if n != ">" and n != "skip" and n != "ski" and gsumtype != "skip" and gsumtype != ">" and gsumtype != "ski":
                if n != "infinity" and n != "inf":
                    sum = a * (1 - comrat ** n) / (1 - comrat)
                else:
                    sum = a / (1 - comrat)
                if round(sum, 12) == 0:
                    sum = 0.0
                print(f"sum = {round(sum, 12)}")
        else:
            rat = 1.0
            print(f"rat (common ratio) = 1.0")
            if n != ">" and n != "skip" and n != "ski" and gsumtype != "skip" and gsumtype != ">" and gsumtype != "ski":
                sum = b * n
                print(f"sum = {round(sum, 12)}")

def polynomial():
    global root
    global root2
    global imag
    global imag2
    global real
    print()
    print("Please enter the equation in the form ax^2 + bx + c = 0, where x is a non-numeric variable name")
    while True:
        clear_variables()
        print()
        a = input('a (i for info): ')
        if a == "<" or a == "exit" or a == "exi":
            break
        elif a == "o" or a == "ope" or a == "operation":
            real_operation()
            break
        elif a == "s" or a == "sum" or a == "summation":
            binomial_expansion()
            break
        elif a == "c" or a == "con" or a == "conic" or a == "conic section":
            conic_section()
            break
        elif a == "sys" or a == "sy" or a == "system" or a == "system of equations":
            system()
            break
        elif a == "info" or a == "inf" or a == "i":
            print()
            print("Please enter a real number or expression as the x^2 coefficient")
            print('Enter "sy" for system of equations, "c" for conic section, "o" for operation (this will direct to real operation) and "s" for summation (this will direct to binomial expansion)')
            continue
        try:
            a = eval(a)
        except:
            print('Please enter a real number or expression, "sy" for system, "c" for conic, "o" for operation, "s" for summation, "i" for info, or "<" to exit')
            continue
        b = input('b: ')
        if b == "<" or b == "exit" or b == "exi":
            continue
        try:
            b = eval(b)
        except:
            print('Please enter a real number or expression, or "<" to exit')
            continue            
        c = input('c: ')   
        if c == "<" or c == "exit" or c == "exi":
            continue
        try:
            c = eval(c)
        except:
            print('Please enter a real number or expression, or "<" to exit')
            continue
        print()
        if round(a, 12) == 0 and round(b, 12) == 0 and round(c, 12) == 0:
            print("Roots: all numbers")
        elif round(a, 12) == 0 and round(b, 12) == 0:
            print("No roots")
        elif round(a, 12) == 0:
            root = -c / b
            print(f"Root: x = {round(root, 12)}")
            print(f"root = {round(root, 12)}")
        else:
            det = b ** 2 - 4 * a * c
            if round(det, 12) > 0:
                root = (-b - sqrt(det)) / (2 * a)
                root2 = (-b + sqrt(det)) / (2 * a)
                print(f"Roots: x = {round(root, 12)} or x = {round(root2, 12)}")
                print(f"root = {round(root, 12)}")
                print(f"root2 = {round(root2, 12)}")
            elif round(det, 12) == 0:
                root = -b / (2 * a)
                print(f"Root: x = {round(root, 12)}")
                print(f"root = {round(root, 12)}")
            else:
                rl = -b / (2 * a)
                im = sqrt(-det) / (2 * a)
                if round(rl, 12) != 0 and round(im, 12) > 0:
                    if round(im, 12) != 1:
                        print(f"Roots: x = {round(rl, 12)} - {round(im, 12)}i or x = {round(rl, 12)} + {round(im, 12)}i")
                    else:
                        print(f"Roots: x = {round(rl, 12)} - i or x = {round(rl, 12)} + i")
                elif round(rl, 12) == 0:
                    if round(im, 12) != 1 and round(im, 12) != -1:
                        print(f"Roots: x = {round(im * -1, 12)}i or x = {round(im, 12)}i")
                    elif round(im, 12) == 1:
                        print(f"Roots: x = -i or x = i")
                    else:
                        print(f"Roots: x = i or x = -i")
                elif round(im, 12) < 0:
                    if round(im, 12) != -1:
                        print(f"Roots: x = {round(rl, 12)} + {round(im * -1, 12)}i or x = {round(rl, 12)} - {round(im * -1, 12)}i")
                    else:
                        print(f"Roots: x = {round(rl, 12)} + i or x = {round(rl, 12)} - i")
                real = rl
                print(f"real (real part) = {round(real, 12)}")
                imag = im * -1
                print(f"imag (imaginary part) = {round(imag, 12)}")
                imag2 = im
                print(f"imag2 (2nd imaginary part) = {round(imag2, 12)}")

def conic_section():
    print("In development!")

def matrix_operation():
    print("In development!")

def system():
    print("In development!")

print("Welcome to Benny's Calculator!")

while True:
    clear_variables()
    print()
    cat = input('Calculation category (i for info): ')
    
    if cat == "exit" or cat == "<" or cat == "exi":
        break
        
    elif cat == "info" or cat == "i" or cat == "inf":
        print()
        print('Categories: operation (o), function (f), summation (s)')
        print()
        
    elif cat == "summation" or cat == "sum" or cat == "s":
        sumtype = input('Summation type (binomial (b), arithmetic (a), geometric (g)): ')
        if sumtype == "<" or sumtype == "exit" or sumtype == "exi":
            continue
        elif sumtype == "b" or sumtype == "binomial" or sumtype == "bin" or sumtype == "binomial expansion":
            binomial_expansion()
        elif sumtype == "a" or sumtype == "arithmetic" or sumtype == "ari" or sumtype == "arithmetic series":
            arithmetic()
        elif sumtype == "geometric" or sumtype == "geo" or sumtype == "g" or sumtype == "geometric series":
            geometric()
        else:
            print('Please enter either "binomial" (b), "arithmetic" (a), "geometric" (g), or "<" to exit')
        
    elif cat == "f" or cat == "fun" or cat == "function":
        funtype = input("Function type (polynomial (p), system (s), conic (c))")
        if funtype == "polynomial" or funtype == "p" or funtype == "pol":
            polynomial()

    elif cat == "operation" or cat == "ope" or cat == "o":
        opetype = input('Operation type (real (r), complex (c), matrix (m)): ')
        if opetype == "<" or opetype == "exit" or opetype == "exi":
            continue
        elif opetype == "real" or opetype == "rea" or opetype == "r":
            real_operation()
        elif opetype == "c" or opetype == "complex" or opetype == "com":
            print()
            ctype = input("From rectangular (r) or polar (p) form: ")
            if ctype == "rectangular" or ctype == "r" or ctype == "rect":
                from_rectangular()
            elif ctype == "polar" or ctype == "p" or ctype == "pol":
                from_polar()
            elif ctype == "<" or ctype == "exit" or ctype == "exi":
                continue
            else:
                print('Please enter either "r" for rectangular, "p" for polar, or "<" to exit')
        elif opetype == "m" or opetype == "mat" or opetype == "matrix":
            matrix_operation()
        else:
            print('Please enter either "r" for real, "c" for complex, "m" for matrix, or "<" to exit')
    
    else:
        print('Please enter either "o" for operation, "f" for function, "s" for summation, "i" for info, or "<" to exit)')

# %% [markdown]
# 

# %%



