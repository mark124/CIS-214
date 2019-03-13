"""
Language processing scanner.

Source: Textbook chapter 10 Parsing and Expression Trees case study student files.
"""

from tokens import Token

class Scanner(object):

    EOE = ';'   # end-of-expression
    TAB = '\t'  # tab

    def __init__(self, sourceStr):
        self._sourceStr = sourceStr
        self._getFirstToken()

    # Returns Token.EOE when the string has been scanned.
    def get(self):
        return self._currentToken

    def hasNext(self):
        return self._currentToken != Token.EOE

    def next(self):
        temp = self._currentToken
        self._getNextToken()
        return temp

    def stringUpToCurrentToken(self):
        return self._sourceStr[0:self._index + 1]

    def _getFirstToken(self):
        self._index = 0
        self._currentChar = self._sourceStr[0]
        self._getNextToken()
    
    def _getInteger(self):
        num = 0
        while True:
            num = num * 10 + int(self._currentChar)
            self._nextChar()
            if not self._currentChar.isdigit():
                break
        return num
    
    def _getNextToken(self):
        self._skipWhiteSpace()
        if self._currentChar.isdigit():
            self._currentToken = Token(self._getInteger())
        elif self._currentChar == Scanner.EOE:
            self._currentToken = Token(';')
        else:
            self._currentToken = Token(self._currentChar)
            self._nextChar()
    
    def _nextChar(self):
        if self._index >= len(self._sourceStr) - 1:
            self._currentChar = Scanner.EOE
        else:
            self._index += 1
            self._currentChar = self._sourceStr[self._index]
    
    def _skipWhiteSpace(self):
        while self._currentChar in (' ', Scanner.TAB):
            self._nextChar()

# A simple tester program:
def main():
    while True:
        sourceStr = input("Enter an expression: ")
        if sourceStr == "": break
        scanner = Scanner(sourceStr)
        token = scanner.get()
        while token.getType() != Token.EOE:
            print(token)
            scanner.next()
            token = scanner.get()

if __name__ == '__main__': 
    main()

