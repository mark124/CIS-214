"""
Expression tree nodes.

Source: Textbook chapter 10 Parsing and Expression Trees case study student files.
"""

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        self._data = data

    def __str__(self):
        return str(self._data)

    # Part 1:
    def infix(self):
        # <your code>
        return str(self)
      
    # Part 2:
    def prefix(self):
        # <your code>
        return str(self)

    def postfix(self):
        return str(self)

    # Part 3:
    def value(self):
        # <your code>
        return self._data

class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, op, leftOper, rightOper):
        self._operator = op
        self._leftOperand = leftOper
        self._rightOperand = rightOper

    # Part 4:
    def infix(self):
        # <your code>
        return "(" + self._leftOperand.infix() + " " + \
               self._operator + " " + \
               self._rightOperand.infix() + ")"

    # Part 5:
    def prefix(self):
        # <your code>
        return self._operator + " " + \
               self._leftOperand.prefix() + " " + \
               self._rightOperand.prefix()
    
    def postfix(self):
        return self._leftOperand.postfix() + " " + \
               self._rightOperand.postfix() + " " + \
               self._operator

    # Part 6:
    def value(self):
        # <your code>
        result = 0
        
        if self._operator == '+':
            return self._leftOperand.value() + self._rightOperand.value()
        if self._operator == '-':
            return self._leftOperand.value() - self._rightOperand.value()
        if self._operator == '^':
            return self._leftOperand.value() ** self._rightOperand.value()
        if self._operator == '*':
             return self._leftOperand.value() * self._rightOperand.value()
        if self._operator == '/':
             return self._leftOperand.value() // self._rightOperand.value()

            
# A simple tester program:
def main():
    a = LeafNode(4)
    b = InteriorNode('+', LeafNode(2), LeafNode(3))
    c = InteriorNode('*', a, b)
    c = InteriorNode('^', c, b) 
    print("Expect ((4 * (2 + 3) ^ (2 + 3)):", c.infix())
    print("Expect ^ * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + ^       :", c.postfix())
    print("Expect 3200000                 :", c.value())

if __name__ == "__main__":
    main()



