"""
Tokens for processing expressions.

Source: Textbook chapter 10 Parsing and Expression Trees case study student files.
"""

class Token(object):

    UNKNOWN  = 0  # unknown
    EOE      = 1  # end-of-expression
    L_PAR    = 2  # left parenthesis
    R_PAR    = 3  # right parenthesis
    
    INT      = 4  # integer
            
    MINUS    = 5  # minus    operator
    PLUS     = 6  # plus     operator
    MUL      = 7  # multiply operator
    DIV      = 8  # divide   operator
    EXPO     = 9  # power    operator

    FIRST_OP = 5  # first operator code

    def __init__(self, value):
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self._makeType(value)
        self._value = value

    def __str__(self):
        return str(self._value)
    
    def getType(self):
       return self._type
    
    def getValue(self):
       return self._value

    def isOperator(self):
        return self._type >= Token.FIRST_OP

    def _makeType(self, ch):
        if   ch == '*': return Token.MUL
        elif ch == '/': return Token.DIV
        elif ch == '+': return Token.PLUS
        elif ch == '-': return Token.MINUS
        elif ch == '(': return Token.L_PAR
        elif ch == ')': return Token.R_PAR
        elif ch == '^': return Token.EXPO
        elif ch == ';': return Token.EOE
        else:           return Token.UNKNOWN;

# A simple tester program:
def main():
    plus = Token("+")
    minus = Token("-")
    mul = Token("*")
    div = Token("/")
    unknown = Token("#")
    anInt = Token(34)
    print(plus, minus, mul, div, unknown, anInt)

if __name__ == '__main__': 
    main()

