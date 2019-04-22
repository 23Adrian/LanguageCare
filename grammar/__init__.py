import  sys

from antlr4 import *
from grammar.CareLangVisitor import CareLangVisitor
from grammar.src.Antlr.careParser import careParser
from grammar.src.Antlr.careLexer import careLexer

def __main__():
    filepath = 'scripts/test.care'
    inputs = FileStream(filepath)
    lexer = careLexer(inputs)
    stream = CommonTokenStream(lexer)
    parser = careParser(stream)
    tree = parser.prog()

    visitor = CareLangVisitor()
    return visitor.visit(tree)

if __name__ == '__main__':
     __main__()
