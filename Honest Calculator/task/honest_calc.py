import sys

memory = 0.0


def is_one_digit(v):
    output = -10 < v < 10 and v.is_integer()
    return output


def check(v1, v2, v3):
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 2) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 in ['*', '+', '-']):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    msg_0 = 'Enter an equation'
    print(msg_0)
    x, oper, y = input().split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        msg_1 = 'Do you even know what numbers are? Stay focused!'
        print(msg_1)
        continue
    if oper not in ('+', '-', '*', '/'):
        msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        print(msg_2)
        continue
    check(x, y, oper)
    if oper == '+':
        result = x + y
        print(result)
    elif oper == '-':
        result = x - y
        print(result)
    elif oper == '*':
        result = x * y
        print(result)
    elif y == 0:
        msg_3 = "Yeah... division by zero. Smart move..."
        print(msg_3)
        continue
    elif oper == '/':
        result = x / y
        print(result)
    while True:
        msg_4 = "Do you want to store the result? (y / n):"
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_10 = "Are you sure? It is only one digit! (y / n)"
                msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
                msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
                msg_index = 10
                while True:
                    if msg_index == 10:
                        print(msg_10)
                    elif msg_index == 11:
                        print(msg_11)
                    elif msg_index == 12:
                        print(msg_12)
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer == 'n':
                        break
                    else:
                        continue
            else:
                memory = result
        elif answer != 'n':
            continue
        while True:
            msg_5 = "Do you want to continue calculations? (y / n):"
            print(msg_5)
            answer = input()
            if answer == 'y':
                break
            if answer == 'n':
                sys.exit()
            continue
        break
