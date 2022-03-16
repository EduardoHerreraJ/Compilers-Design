# Generated from c:\Users\lalo2\OneDrive\Escritorio\8vo Semestre\Diseño de compiladores\1er Parcial\marzo\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#asignacion.
    def visitAsignacion(self, ctx:marzoParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#numero.
    def visitNumero(self, ctx:marzoParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#mayor.
    def visitMayor(self, ctx:marzoParser.MayorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#menor.
    def visitMenor(self, ctx:marzoParser.MenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#char.
    def visitChar(self, ctx:marzoParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#resta.
    def visitResta(self, ctx:marzoParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#endStatement.
    def visitEndStatement(self, ctx:marzoParser.EndStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#print.
    def visitPrint(self, ctx:marzoParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaracion.
    def visitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#if.
    def visitIf(self, ctx:marzoParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifElse.
    def visitIfElse(self, ctx:marzoParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#asignacionExp.
    def visitAsignacionExp(self, ctx:marzoParser.AsignacionExpContext):
        return self.visitChildren(ctx)



del marzoParser