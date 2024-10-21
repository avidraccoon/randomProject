encoded = ""
formated = False
tab_count = 0
def append(text):
    global encoded
    encoded += text

def new_line(forced=False):
    global encoded
    if formated or forced: append("\n" + "\t"*tab_count)

def move_left(times = 1):
    append("<" * times)

def move_right(times = 1):
    append(">" * times)

def increment():
    append("^")

def decrement():
    append("_")

def output():
    append(".")

def loop_start():
    global tab_count
    new_line()
    append("[")
    tab_count+=1

def loop_end():
    global tab_count
    tab_count-=1
    new_line()
    append("]")

def address():
    append("@")

def program_address():
    append("?")

def goto():
    append("%")

def goto_program():
    append("$")

def go_home():
    append("!")

def display():
    append("d")

def add():
    append("+")

def sub():
    append("-")

def multiply():
    append("*")

def divide():
    append("/")

def store_a():
    append("a")

def get_a():
    append("A")

def store_b():
    append("b")

def get_b():
    append("B")

def store_c():
    append("c")

def get_c():
    append("C")

def set_value(value):
    append("("+str(value)+")")

def text(text):
    if formated: append(text)

def label():
    append("|")

def goto_label():
    append("~")