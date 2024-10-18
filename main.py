import language
from language import move_left, move_right, loop_start, loop_end, increment, decrement, go_home, goto, replace, output, address, new_line

with open("program.txt") as file:
    program = file.read()

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
# & - use pointer value for next operation
# ! - go home

# new commands
# a - set a
# b - set b
# c - set c
# A - get A
# B - get B
# C - get C

# math commands /Result goes in A and B is not safe trashes pointer and pointer +1
# + - adds reg A and B
# - - subtracts A and B
# * - multiplies A and B
# / - divides A and B

# reserverd pointers
# 0 - Address
# 1 - home ret
# 2 - reg A
# 3 - reg B
# 4 - reg C
# 5 - trash
prefix = ""
comment = False
#prefix = ">>"*5
language.formated = True
def store_a():
    loop_start()
    new_line()
    decrement()
    move_right()
    increment()
    move_left()
    go_home()
    move_right(2)
    increment()
    move_left()
    goto()
    loop_end()
    new_line()
    move_right()
    loop_start()
    new_line()
    decrement()
    move_left()
    increment()
    move_right()
    loop_end()
    new_line()
    move_left()

def store_b():
    loop_start()
    new_line()
    decrement()
    move_right()
    increment()
    move_left()
    go_home()
    move_right(3)
    increment()
    move_left(2)
    goto()
    loop_end()
    new_line()
    move_right()
    loop_start()
    new_line()
    decrement()
    move_left()
    increment()
    move_right()
    loop_end()
    new_line()
    move_left()

def store_c():
    loop_start()
    new_line()
    decrement()
    move_right()
    increment()
    move_left()
    go_home()
    move_right(4)
    increment()
    move_left(3)
    goto()
    loop_end()
    new_line()
    move_right()
    loop_start()
    new_line()
    decrement()
    move_left()
    increment()
    move_right()
    loop_end()
    new_line()
    move_left()

def get_a():
    go_home()
    move_right(2)
    loop_start()
    new_line()
    decrement()
    move_right(3)
    increment()
    move_left(4)
    goto()
    increment()
    go_home()
    move_right(2)
    loop_end()
    new_line()
    move_right(3)
    loop_start()
    new_line()
    decrement()
    move_left()
    increment()
    move_right()
    loop_end()
    new_line()
    move_left(4)
    goto()

def get_b():
    go_home()
    move_right(3)
    loop_start()
    new_line()
    decrement()
    move_right(2)
    increment()
    move_left(4)
    goto()
    increment()
    go_home()
    move_right(3)
    loop_end()
    new_line()
    move_right(2)
    loop_start()
    new_line()
    decrement()
    move_left()
    increment()
    move_right()
    loop_end()
    new_line()
    move_left(4)
    goto()

def get_c():
    go_home()
    move_right(4)
    loop_start()
    new_line()
    decrement()
    move_right()
    increment()
    move_left(4)
    goto()
    increment()
    go_home()
    move_right(4)
    loop_end()
    new_line()
    move_right()
    loop_start()
    new_line()
    decrement()
    move_left()
    increment()
    move_right()
    loop_end()
    new_line()
    move_left(4)
    goto()


def encode():
    global encoded, comment
    for char in program:
        if comment:
            if (char == "\n"):
                comment = False
            continue
        match char:
            case "<":
                move_left()
                move_left()
            case ">":
                move_right()
                move_right()
            case "^":
                increment()
            case "_":
                decrement
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
            case "&":
                replace()
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
            case "#":
                comment = True
                continue
            case " ":
                continue
        language.new_line()
        language.new_line()

    with open("encoded_program.txt", "w") as file:
        file.write(prefix+language.encoded)



encode()