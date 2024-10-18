import time
class Intepreter:

    def __init__(self, memory_size):
        self.program_pointer = 0
        self.memory_pointer = 0
        self.memory = [0 for i in range(memory_size)]
        self.loops = []
        self.skipping = 0
        self.instructions = 0
        self.debug = False
        self.labels = []

    def label(self):
        self.labels.push(self.memory_pointer)

    def goto_label(self):
        if self.get_memory() < 0 or self.get_memory() > len(self.labels):
            pass
        self.program_pointer = self.labels[self.get_memory()]

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
            if self.instructions > 20000:
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
            if char == "d":
                #self.display()
                pass
            self.program_pointer+=1
            if self.debug: print(self.memory_pointer, self.program_pointer, char, self.skipping, self.loops, self.memory)