import time
class Intepreter:

    def __init__(self, memory_size):
        self.program_pointer = 0
        self.memory_pointer = 0
        self.memory = [0 for i in range(memory_size)]
        self.loops = []
        self.variables = {}
        self.functions = {}
        self.skipping = 0
        self.instructions = 0
        self.debug = False
        self.name = ""
        self.naming = True
        self.variable = False

    def handle_name(self):
        if len(self.program)<=self.program_pointer+1:
            self.set_memory(self.variables[self.name])
        elif (self.program[self.program_pointer+1] == ":"):
            self.program_pointer+=1
        elif self.program[self.program_pointer+1] in ["~", "`"]:
            if self.program[self.program_pointer+1] != "`":
                self.set_memory(self.functions[self.name])
        else:
            self.set_memory(self.variables[self.name])
        
    def create_variable(self):
        self.variable = True

    def quote(self):
        name = ""
        while self.program[self.program_pointer+1] != "\"":
            self.program_pointer+=1
            name += self.program[self.program_pointer]
        self.program_pointer+=1
        if self.variable:
            self.variables[name] = self.get_memory()
        else:
            self.name = name
            self.handle_name()
        self.variable = False


    def label(self):
        self.functions[self.name] = self.program_pointer
        while self.program[self.program_pointer+1] != ";":
            self.program_pointer+=1
        self.program_pointer+=1
        self.name = ""

    def goto_label(self):
        self.memory[5] = self.program_pointer
        self.program_pointer = self.get_memory()

    def get_memory(self):
        return self.memory[self.memory_pointer]

    def set_memory(self, value):
        self.memory[self.memory_pointer] = value

    def inc(self):
        self.set_memory(self.get_memory()+1)

    def dec(self):
        self.set_memory(self.get_memory()-1)

    def add(self):
        self.memory[2] = self.memory[2] + self.memory[3]

    def subtract(self):
        self.memory[2] = self.memory[2] - self.memory[3]

    def multiply(self):
        self.memory[2] = self.memory[2] * self.memory[3]

    def divide(self):
        self.memory[2] = self.memory[2] / self.memory[3]

    def get_a(self):
        self.set_memory(self.memory[2])

    def store_a(self):
        self.memory[2] = self.get_memory()

    def get_b(self):
        self.set_memory(self.memory[3])

    def store_b(self):
        self.memory[3] = self.get_memory()

    def get_c(self):
        self.set_memory(self.memory[4])

    def store_c(self):
        self.memory[4] = self.get_memory()

    def left(self):
        self.memory_pointer -= 1

    def right(self):
        self.memory_pointer += 1

    def start(self):
        if self.get_memory() == 0:
            self.skipping += 1
        else:
            self.loops.append(self.program_pointer)

    def end(self):
        if self.skipping>0:
            self.skipping -= 1
        else:
            self.program_pointer = self.loops.pop()-1
    
    def out(self):
        print(self.get_memory())

    def program_address(self):
        self.program_pointer = self.get_memory()

    def address(self):
        self.set_memory(self.memory_pointer)
    
    def mem_goto(self):
        self.memory_pointer = self.get_memory()

    def go_home(self):
        self.memory[1] = self.memory_pointer
        self.memory_pointer = 0

    def display(self):
        print(self.memory_pointer, self.program_pointer, self.skipping, self.loops, self.memory)

    def value(self):
        num = ""
        while self.program[self.program_pointer+1] != ")":
            self.program_pointer+=1
            num += self.program[self.program_pointer]
        self.program_pointer+=1
        self.set_memory(int(num))

    def run(self, program):
        self.program = program
        while self.program_pointer<len(program):
            #time.sleep(.1)
            char = program[self.program_pointer]
            self.instructions += 1
            if self.instructions > 400:
                self.display()
                print("fail safe")
                break
            if self.skipping > 0:
                if char == "[":
                    self.skipping+=1
                if char == "]":
                    self.end()
            else:
                match char:
                    case "^": self.inc()
                    case "_": self.dec()
                    case "<": self.left()
                    case ">": self.right()
                    case "[": self.start()
                    case "]": self.end()
                    case ".": self.out()
                    case "@": self.address()
                    case "!": self.go_home()
                    case "%": self.mem_goto()
                    case "d": self.display()
                    case "+": self.add()
                    case "-": self.subtract()
                    case "*": self.multiply()
                    case "/": self.divide()
                    case "a": self.store_a()
                    case "b": self.store_b()
                    case "c": self.store_c()
                    case "A": self.get_a()
                    case "B": self.get_b()
                    case "C": self.get_c()
                    case "(": self.value()
                    case "|": self.label()
                    case "~": self.goto_label()
                    case "=": self.create_variable()
                    case "\"": self.quote()
                    case "$": self.program_address()
                    case "?": (lambda self: self.set_memory(self.program_pointer))(self)
            if char == "d":
                #self.display()
                pass
            self.program_pointer+=1
            if self.debug: print(self.memory_pointer, self.program_pointer, char, self.skipping, self.loops, self.memory)