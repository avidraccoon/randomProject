import interpret, main
size = 20

program = "^ab>^^^^[_<A.+b>]"
#program = "^^_"
compiled = main.encode(program)

print(compiled)
interpreter = interpret.Intepreter(size)
interpreter.debug = False
interpreter.run(compiled)
print(interpreter.memory_pointer, interpreter.program_pointer, interpreter.skipping, interpreter.loops, interpreter.memory)