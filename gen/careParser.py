# Generated from C:/Users/adria/PycharmProjects/LanguageCare/grammar/src\care.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\7\3")
        buf.write("\17\n\3\f\3\16\3\22\13\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\7\5\34\n\5\f\5\16\5\37\13\5\3\5\2\3\b\6\2\4\6\b\2\2")
        buf.write("\2\36\2\n\3\2\2\2\4\20\3\2\2\2\6\23\3\2\2\2\b\25\3\2\2")
        buf.write("\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3\3\2\2\2\r\17\5\6\4\2")
        buf.write("\16\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2")
        buf.write("\2\21\5\3\2\2\2\22\20\3\2\2\2\23\24\5\b\5\2\24\7\3\2\2")
        buf.write("\2\25\26\b\5\1\2\26\27\7\16\2\2\27\35\3\2\2\2\30\31\f")
        buf.write("\4\2\2\31\32\7\b\2\2\32\34\5\b\5\5\33\30\3\2\2\2\34\37")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\t\3\2\2\2\37\35")
        buf.write("\3\2\2\2\4\20\35")
        return buf.getvalue()


class careParser ( Parser ):

    grammarFileName = "care.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'-'", "'+'", "'*'", "'^'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'si'" ]

    symbolicNames = [ "<INVALID>", "DIV", "MINUS", "PLUS", "MULTIPLY", "EXPO", 
                      "OPERATOR", "NEWLINE", "WS", "LINE_COMMENT", "IF", 
                      "SI", "INT", "STRING" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_exp = 3

    ruleNames =  [ "prog", "statements", "statement", "exp" ]

    EOF = Token.EOF
    DIV=1
    MINUS=2
    PLUS=3
    MULTIPLY=4
    EXPO=5
    OPERATOR=6
    NEWLINE=7
    WS=8
    LINE_COMMENT=9
    IF=10
    SI=11
    INT=12
    STRING=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(careParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(careParser.EOF, 0)

        def getRuleIndex(self):
            return careParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = careParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.statements()
            self.state = 9
            self.match(careParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(careParser.StatementContext)
            else:
                return self.getTypedRuleContext(careParser.StatementContext,i)


        def getRuleIndex(self):
            return careParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = careParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==careParser.INT:
                self.state = 11
                self.statement()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(careParser.ExpContext,0)


        def getRuleIndex(self):
            return careParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = careParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(careParser.INT, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(careParser.ExpContext)
            else:
                return self.getTypedRuleContext(careParser.ExpContext,i)


        def OPERATOR(self):
            return self.getToken(careParser.OPERATOR, 0)

        def getRuleIndex(self):
            return careParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = careParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(careParser.INT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = careParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 22
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 23
                    self.match(careParser.OPERATOR)
                    self.state = 24
                    self.exp(3) 
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




