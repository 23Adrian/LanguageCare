import  sys

from antlr4 import *
from grammar.CareLangVisitor import CareLangVisitor
from grammar.Build.careParser import careParser
from grammar.Build.careLexer import careLexer

def __main__():
    """

    :rtype: object
    """
    filepath = 'scripts/test.care'
    inputs = FileStream(filepath)
    lexer = careLexer(inputs)
    stream = CommonTokenStream(lexer)
    parser = careParser(stream)
    tree = parser.prog()

    visitor = CareLangVisitor()
    return visitor.visit(tree)

if __name__ == '    main    ':
     __main__()
