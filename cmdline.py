from pybrain import BrainFuck_Int
import time

version = "0.1.0"

tape = [0] * 30000
pointer = 0

print """PyBrain v{} (Wil Steadman)""".format(version)

counter = 1
while True:
    prog = raw_input("pb ({}) #".format(counter))
    time1 = time.time()
    interpreter = BrainFuck_Int(prog, tape, pointer)
    time2 = time.time()
    
    tape = interpreter.tape
    pointer = interpreter.cellPtr

    print time2 - time1
    
    counter += 1
