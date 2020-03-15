# Evaluation challenge for the discipline of Fundamentals of Computational Problems I.
# In the course of Information system at Federal Rural University of Pernambuco.
# Student: José Vitor - @jszvitor
# Teacher: Cícero Garrozi - 
# 02-Complexity - simple version - [run.codes]

class Stack:
    def __init__(self):
        self.items = []
        """
        constructor of the class
        """
    def isEmpty(self):
        """
        returns a boolean value. Where True is for the empty stack.
        """
        return self.items == []

    def push(self, item):
        """
        returns the addiction of an element in the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        returns the last element in the stack and removing it.
        """
        return self.items.pop()

    def peek(self):
        """
        returns the last element in the stack without removing it.
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
        returns the stack size.
        """
        return len(self.items)
    def stack(self):
        """
        returns the stack elements
        """
        return self.items

def ComplexityCalc(string):
    algorithm = Stack()
    entrada = string.split()
    try:
        while len(entrada) > 0:
            if 'FIM' == entrada[-1]:
                algorithm.push(')')
                entrada.pop()
            elif 'OP' == entrada[-1]:
                algorithm.push('+')
                entrada.pop()
            elif 'LOOP' == entrada[-1]:
                algorithm.push('+{}*('.format(algorithm.pop()))
                entrada.pop()
            elif 'INICIO' == entrada[-1]:
                algorithm.push('(')
                entrada.pop()
            else:
                algorithm.push(entrada.pop())
            
            result = ''.join(algorithm.stack()[::-1])
            # '(+3+2*(+10*(+1)))'

    except Exception as e:
        return e
    finally:
        return eval(result)

def main():
    # input: "INICIO OP 3 LOOP 2 LOOP 10 OP 1 FIM FIM FIM"
    string = input()
    print(ComplexityCalc(string))
    # output: 23

if __name__ == "__main__":
    main()