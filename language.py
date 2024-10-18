encoded = ""
formated = False
tab_count = 0
def new_line():
    global encoded
    if formated: encoded += "\n" + "\t"*tab_count

def move_left(times = 1):
    global encoded
    encoded += "<" * times

def move_right(times = 1):
    global encoded
    encoded += ">" * times

def increment():
    global encoded
    encoded += "^"

def decrement():
    global encoded
    encoded += "_"

def output():
    global encoded
    encoded += "."

def loop_start():
    global encoded,tab_count
    new_line()
    encoded += "["
    tab_count+=1

def loop_end():
    global encoded,tab_count
    tab_count-=1
    new_line()
    encoded += "]"

def address():
    global encoded
    encoded += "@"

def program_address():
    global encoded
    encoded += "?"

def goto():
    global encoded
    encoded += "%"

def goto_program():
    global encoded
    encoded += "$"

def replace():
    global encoded
    encoded += "&"

def go_home():
    global encoded
    encoded += "!"