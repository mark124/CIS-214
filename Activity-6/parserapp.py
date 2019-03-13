"""
View for the infix expression parser.
Handles user interaction.

Source: Textbook chapter 10 Parsing and Expression Trees case study student files.
"""

from parsers import Parser

class ParserView(object):

    def run(self):
        parser = Parser()
        while True:
            sourceStr = input("Enter an infix expression: ")
            if sourceStr == "": break
            try:
                tree = parser.parse(sourceStr)
                print("Prefix:", tree.prefix())
                print("Infix:", tree.infix())
                print("Postfix:", tree.postfix())
                print("Value:", tree.value())
            except Exception as e:
                print("Error:")
                print(e)

ParserView().run()
