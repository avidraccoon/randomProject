import language
from language import move_left, move_right, loop_start, loop_end, increment, decrement, go_home, goto, output, address, new_line, add, sub, multiply, divide, get_a, get_c, get_b, store_a, store_b, store_c, goto_program, label, goto_label, program_address

fib = "^ab>^^^[_<A+b>]"
with open("program.txt") as file:
    program = file.read()
#program = fib
# default commands
# ^ - increment
# _ - decrement
# < - move_left
# > - move_right
# [ - loop start
# ] - loop end
# . - output pointer
# @ - set pointer to address
# ? - set pointer to program address
# % - memory pointer goto pointer value
# $ - program pointer goto pointer value
# ! - go home
# & - call
# a - set a
# b - set b
# c - set c
# A - get A
# B - get B
# C - get C
# (value) - set pointer to value
# | - create label
# ~ - goto label

# math commands /Result goes in A
# + - adds reg A and B
# - - subtracts A and B
# * - multiplies A and B
# / - divides A and B

# new commands
# { - push
# } - pop
# & - call




# reserverd pointers
# 0 - Address
# 1 - home ret
# 2 - reg A
# 3 - reg B
# 4 - reg C
# 5 - ret store
# 6 - stack pointer
# 7 - trash
# 8 - trash
# 9 - trash
# 10 - trash

trash_location = 6
prefix = ""
comment = False
value = False
stack_pos = 24

prefix = ">"*6+"("+str(stack_pos)+")"+">"*4
#program = "*"
language.formated = False
newLines = False

def display():
    language.display()

def clear_pointer():
    loop_start()
    new_line()
    decrement()
    loop_end()
    new_line()

def set_value(value):
    clear_pointer()
    language.set_value(value)

def goto_ret():
    go_home()
    move_right()

def goto_trash():
    go_home()
    move_right(trash_location)
    
def return_from_trash():
    move_left(trash_location)
    go_home()

def store_ret():
    go_home()
    move_right()
    store_c()
    move_right(4)
    get_c()
    move_left(4)
    goto()

def restore_ret():
    go_home()
    move_right()
    store_b()
    move_right(4)
    store_c()
    get_b()
    move_left(4)
    get_c()
    move_right(4)
    goto()

def goto_stack():
    go_home()
    move_right(6)
    goto()

def push():
    store_ret()
    store_c()
    goto_stack()
    get_c()
    go_home()
    move_right(6)
    store_a()
    move_left(3)
    set_value(1)
    sub()
    move_right(3)
    get_a()
    goto_ret()
    restore_ret()
    goto()

def pop():
    store_ret()
    go_home()
    move_right(6)
    store_a()
    move_left(3)
    set_value(1)
    add()
    move_right(3)
    get_a()
    goto_stack()
    store_a()
    goto_ret()
    restore_ret()
    goto()
    get_a()
    
def call():
    store_b()
    program_address()
    push()
    get_b()
    goto_label()

def encode(program):
    global encoded, comment, value
    for char in program:
        if char.isnumeric() and value:
            language.append(char)
            continue
        if comment:
            if (char == "\n"):
                comment = False
            else:
                language.text(char)
            continue
        match char:
            case "<":
                move_left()
                #move_left()
            case ">":
                move_right()
                #move_right()
            case "^":
                increment()
            case "_":
                decrement()
            case "[":
                loop_start()
            case "]":
                loop_end()
            case ".":
                output()
            case "@":
                address()
            case "$":
                goto()
            case "!":
                go_home()
            case "a":
                store_a()
            case "b":
                store_b()
            case "c":
                store_c()
            case "A":
                get_a()
            case "B":
                get_b()
            case "C":
                get_c()
            case "+":
                add()
            case "-":
                sub()
            case "*":
                multiply()
            case "/":
                divide()
            case "{":
                push()
            case "}":
                pop()
            case "&":
                call()
            case "|":
                label()
            case "~":
                goto_label()
            case "(":
                value = True
                language.append("(")
                continue
            case ")":
                value = False
                language.append(")")
                continue
            case "#":
                comment = True
                continue
            case " ":
                continue
        language.new_line(newLines)
        language.new_line(newLines)
    return prefix+language.encoded


if __name__ == "__main__":
    with open("encoded_program.txt", "w") as file:
        file.write(encode(program))