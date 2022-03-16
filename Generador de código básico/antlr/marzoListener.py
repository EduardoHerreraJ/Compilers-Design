# Generated from c:\Users\lalo2\OneDrive\Escritorio\8vo Semestre\Diseño de compiladores\1er Parcial\marzo\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#asignacion.
    def enterAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass

    # Exit a parse tree produced by marzoParser#asignacion.
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass


    # Enter a parse tree produced by marzoParser#numero.
    def enterNumero(self, ctx:marzoParser.NumeroContext):
        pass

    # Exit a parse tree produced by marzoParser#numero.
    def exitNumero(self, ctx:marzoParser.NumeroContext):
        pass


    # Enter a parse tree produced by marzoParser#mayor.
    def enterMayor(self, ctx:marzoParser.MayorContext):
        pass

    # Exit a parse tree produced by marzoParser#mayor.
    def exitMayor(self, ctx:marzoParser.MayorContext):
        pass


    # Enter a parse tree produced by marzoParser#menor.
    def enterMenor(self, ctx:marzoParser.MenorContext):
        pass

    # Exit a parse tree produced by marzoParser#menor.
    def exitMenor(self, ctx:marzoParser.MenorContext):
        pass


    # Enter a parse tree produced by marzoParser#char.
    def enterChar(self, ctx:marzoParser.CharContext):
        pass

    # Exit a parse tree produced by marzoParser#char.
    def exitChar(self, ctx:marzoParser.CharContext):
        pass


    # Enter a parse tree produced by marzoParser#resta.
    def enterResta(self, ctx:marzoParser.RestaContext):
        pass

    # Exit a parse tree produced by marzoParser#resta.
    def exitResta(self, ctx:marzoParser.RestaContext):
        pass


    # Enter a parse tree produced by marzoParser#endStatement.
    def enterEndStatement(self, ctx:marzoParser.EndStatementContext):
        pass

    # Exit a parse tree produced by marzoParser#endStatement.
    def exitEndStatement(self, ctx:marzoParser.EndStatementContext):
        pass


    # Enter a parse tree produced by marzoParser#print.
    def enterPrint(self, ctx:marzoParser.PrintContext):
        pass

    # Exit a parse tree produced by marzoParser#print.
    def exitPrint(self, ctx:marzoParser.PrintContext):
        pass


    # Enter a parse tree produced by marzoParser#declaracion.
    def enterDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by marzoParser#declaracion.
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by marzoParser#if.
    def enterIf(self, ctx:marzoParser.IfContext):
        pass

    # Exit a parse tree produced by marzoParser#if.
    def exitIf(self, ctx:marzoParser.IfContext):
        pass


    # Enter a parse tree produced by marzoParser#ifElse.
    def enterIfElse(self, ctx:marzoParser.IfElseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifElse.
    def exitIfElse(self, ctx:marzoParser.IfElseContext):
        pass


    # Enter a parse tree produced by marzoParser#asignacionExp.
    def enterAsignacionExp(self, ctx:marzoParser.AsignacionExpContext):
        pass

    # Exit a parse tree produced by marzoParser#asignacionExp.
    def exitAsignacionExp(self, ctx:marzoParser.AsignacionExpContext):
        pass



del marzoParser