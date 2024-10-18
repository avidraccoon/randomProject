
class Intepreter:

    def __init__(self, memory_size):
        self.program_pointer = 0
        self.memory_pointer = 6
        self.memory = [0 for i in range(memory_size)]
        self.loops = []
        self.skipping = 0
        self.instructions = 0
        self.debug = False

    def get_memory(self):
        return self.memory[self.memory_pointer]

    def set_memory(self, value):
        self.memory[self.memory_pointer] = value

    def inc(self):
        self.set_memory(self.get_memory()+1)

    def dec(self):
        self.set_memory(self.get_memory()-1)

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

    def run(self, program):
        while self.program_pointer<len(program):
            char = program[self.program_pointer]
            self.instructions += 1
            if self.instructions > 2000:
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
            self.program_pointer+=1
            if self.debug: print(self.memory_pointer, self.program_pointer, char, self.skipping, self.loops, self.memory)