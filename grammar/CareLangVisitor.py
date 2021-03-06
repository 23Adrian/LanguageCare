from grammar.src.Antlr.careParser import careParser
from grammar.src.Antlr.careVisitor import careVisitor as careLangOrigin



class CareLangVisitor(careLangOrigin):
    # Visit a parse tree produced by careParser#prog.
    def visitProg(self, ctx: careParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by careParser#statements.
    def visitStatements(self, ctx: careParser.StatementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by careParser#statement.
    def visitStatement(self, ctx: careParser.StatementContext):
        print("made a statement")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by careParser#finished.
    def visitFinished(self, ctx:careParser.FinishedContext):

        result = None

        if(ctx.exp()):
            result = self.visit(ctx.exp())
            print("the result is :" + str(result))

        else:
            result = self.visitChildren(ctx)
            print("not a success =(")

        return  result


    # Visit a parse tree produced by careParser#exp.
    def visitExp(self, ctx: careParser.ExpContext):
        if(ctx.INT()):
            return int(ctx.INT().getText())

        if(ctx.LParen()):
            return self.visit(ctx.exp(0))

        if(ctx.PLUS()):

            return self.visitExp(ctx.exp(0)) + self.visitExp(ctx.exp(1))

        if (ctx.MINUS()):
            return self.visitExp(ctx.exp(0)) + (self.visitExp(ctx.exp(1)) * -1)

        if (ctx.MULTIPLY()):
            return self.visitExp(ctx.exp(0)) * self.visitExp(ctx.exp(1))

        if (ctx.DIV()):
            return self.visitExp(ctx.exp(0)) / self.visitExp(ctx.exp(1))

        if(ctx.EXPO()):
            return  self.visitExp(ctx.exp(0)) ** self.visitExp(ctx.exp(1))

        return self.visitChildren(ctx)






