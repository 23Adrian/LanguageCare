# Generated from C:/Users/adria/PycharmProjects/LanguageCare/grammar/src\care.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\61\n\7\3\b\5\b\64")
        buf.write("\n\b\3\b\3\b\3\b\3\b\3\t\6\t;\n\t\r\t\16\t<\3\t\3\t\3")
        buf.write("\n\3\n\3\n\7\nD\n\n\f\n\16\nG\13\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\r\6\rR\n\r\r\r\16\rS\3\16\6\16W\n\16")
        buf.write("\r\16\16\16X\3\17\3\17\3\20\5\20^\n\20\2\2\21\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\2\37\2\3\2\6\4\2\13\13\"\"\4\2\f\f\17\17\3\2\62;\4")
        buf.write("\2C\\c|\2e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2")
        buf.write("\2\2\13)\3\2\2\2\r\60\3\2\2\2\17\63\3\2\2\2\21:\3\2\2")
        buf.write("\2\23@\3\2\2\2\25J\3\2\2\2\27M\3\2\2\2\31Q\3\2\2\2\33")
        buf.write("V\3\2\2\2\35Z\3\2\2\2\37]\3\2\2\2!\"\7\61\2\2\"\4\3\2")
        buf.write("\2\2#$\7/\2\2$\6\3\2\2\2%&\7-\2\2&\b\3\2\2\2\'(\7,\2\2")
        buf.write("(\n\3\2\2\2)*\7`\2\2*\f\3\2\2\2+\61\5\3\2\2,\61\5\t\5")
        buf.write("\2-\61\5\7\4\2.\61\5\5\3\2/\61\5\13\6\2\60+\3\2\2\2\60")
        buf.write(",\3\2\2\2\60-\3\2\2\2\60.\3\2\2\2\60/\3\2\2\2\61\16\3")
        buf.write("\2\2\2\62\64\7\17\2\2\63\62\3\2\2\2\63\64\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\66\7\f\2\2\66\67\3\2\2\2\678\b\b\2\28\20\3")
        buf.write("\2\2\29;\t\2\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2")
        buf.write("\2=>\3\2\2\2>?\b\t\2\2?\22\3\2\2\2@A\5\3\2\2AE\5\3\2\2")
        buf.write("BD\n\3\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3")
        buf.write("\2\2\2GE\3\2\2\2HI\b\n\3\2I\24\3\2\2\2JK\7k\2\2KL\7h\2")
        buf.write("\2L\26\3\2\2\2MN\7u\2\2NO\7k\2\2O\30\3\2\2\2PR\5\35\17")
        buf.write("\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\32\3\2\2\2")
        buf.write("UW\5\37\20\2VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y")
        buf.write("\34\3\2\2\2Z[\t\4\2\2[\36\3\2\2\2\\^\t\5\2\2]\\\3\2\2")
        buf.write("\2^ \3\2\2\2\n\2\60\63<ESX]\4\b\2\2\2\3\2")
        return buf.getvalue()


class careLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DIV = 1
    MINUS = 2
    PLUS = 3
    MULTIPLY = 4
    EXPO = 5
    OPERATOR = 6
    NEWLINE = 7
    WS = 8
    LINE_COMMENT = 9
    IF = 10
    SI = 11
    INT = 12
    STRING = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'/'", "'-'", "'+'", "'*'", "'^'", "'if'", "'si'" ]

    symbolicNames = [ "<INVALID>",
            "DIV", "MINUS", "PLUS", "MULTIPLY", "EXPO", "OPERATOR", "NEWLINE", 
            "WS", "LINE_COMMENT", "IF", "SI", "INT", "STRING" ]

    ruleNames = [ "DIV", "MINUS", "PLUS", "MULTIPLY", "EXPO", "OPERATOR", 
                  "NEWLINE", "WS", "LINE_COMMENT", "IF", "SI", "INT", "STRING", 
                  "DIGIT", "LETTER" ]

    grammarFileName = "care.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


