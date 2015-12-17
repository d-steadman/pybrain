from sys import stdin, stdout

class BrainFuck_Int(object):
    def __init__(self, prog, tape, cellPtr):
        self.prog = prog
        self.tape = tape
        self.cellPtr = cellPtr
        self.pc = 0
        self.stack = []
        self.jumpTable = [None] * len(self.prog)
        
        self.build_jump_table()
        self.execute()

        self.pc = 0
        for cell in self.tape:
            if cell != 0:
                print "{}: [{}]".format(self.pc, self.tape[self.pc])

            else:
                pass
            
            self.pc += 1

        print "pointer: [{}]".format(str(self.cellPtr))
        
    def build_jump_table(self): # Builds a reference table for loops
        for num, char in enumerate(self.prog):
            if char == "[":
                self.stack.append(num)
                
            if char == "]":
                self.jumpTable[num] = self.stack.pop()
                self.jumpTable[self.jumpTable[num]] = num
        
    def execute(self):
        while self.pc < len(self.prog):
            if self.prog[self.pc] == ">":   # Adds one to the cell pointer
                if self.cellPtr + 1 > len(self.tape):
                    print "[ERROR(INDEX)]: Cell pointer out of range: {}".format(self.cellPtr + 1)

                else:
                    self.cellPtr += 1
                    
            if self.prog[self.pc] == "<":   # Subtracts one from the cell pointer
                if self.cellPtr - 1 < 0:
                    print "[ERROR(INDEX)]: Cell pointer out of range: {}".format(self.cellPtr - 1)

                else:
                    self.cellPtr -= 1
                
            if self.prog[self.pc] == "+":   # Adds one to the current cell
                if self.tape[self.cellPtr] + 1 > 255:
                    print "[ERROR(OVERFLOW)]: 8-Bit limit exceeded: {}".format(self.tape[self.cellPtr] + 1)

                else:
                    self.tape[self.cellPtr] += 1
                
            if self.prog[self.pc] == "-":   # Subtracts one to the current cell
                if self.tape[self.cellPtr] - 1 < -256:
                    print "[ERROR(OVERFLOW)]: 8-Bit limit exceeded: {}".format(self.tape[self.cellPtr] - 1)

                else:
                    self.tape[self.cellPtr] -= 1
            
            if self.prog[self.pc] == ",":   # Takes a single char as an ordinal
                self.tape[self.cellPtr] = ord(raw_input()[0])
                    
                
            if self.prog[self.pc] == ".":   # Prints the int in the current cell as a char
                stdout.write(chr(self.tape[self.cellPtr]) + "\n")
                
            if self.prog[self.pc] == "[" and self.tape[self.cellPtr] == 0:   # Beginning of loop
                self.pc = self.jumpTable[self.pc]
                
            if self.prog[self.pc] == "]" and self.tape[self.cellPtr]:       # End of loop
                self.pc = self.jumpTable[self.pc]
                
            self.pc += 1
