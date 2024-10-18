import interpret, main
size = 50

program = "(4){"
main.language.formated = False
compiled = main.encode(program)
print(compiled)
interpreter = interpret.Intepreter(size)
interpreter.debug = True
interpreter.run(compiled)

print(interpreter.memory_pointer, interpreter.program_pointer, interpreter.skipping, interpreter.loops, interpreter.memory)