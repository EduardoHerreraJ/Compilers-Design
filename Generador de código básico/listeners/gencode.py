from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

class GenCode(marzoListener):

    def __init__(self):
        self.x = 0
        self.list = []
        self.list2 = []
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    #--------------------EXPRESSION ----------------------------
    #NUMERO
    def exitNumero(self, ctx: marzoParser.NumeroContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("li $v" + str(self.x) + ", " + ctx.Numero().getText())

    #CHAR
    def exitChar(self, ctx: marzoParser.CharContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("lw $v" + str(self.x) + ", " + ctx.Char().getText())

    #SUMA
    def exitSuma(self, ctx:marzoParser.SumaContext):
        print("ADD $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    #RESTA
    def exitResta(self, ctx: marzoParser.RestaContext):
        print("REST $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))
    
    #Asignación
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        print("li $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    #COMPARACIÓN MENOR
    def exitMenor(self, ctx:marzoParser.MenorContext):
        print("sllower $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))
    
    #COMPARACIÓN MAYOR
    def exitMayor(self, ctx:marzoParser.MayorContext):
        print("stgreater $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))
    
    #--------------------STATMENT ----------------------------
    #IF
    def exitIf(self, ctx: marzoParser.IfContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)))

    #IF ELSE
    def exitIfElse(self, ctx:marzoParser.IfElseContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)) + ", ELSE")

    #DECLARACIÓN
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("sw $v" + str(self.x) + ", " + ctx.Char().getText())
    
    #PRINT
    def exitPrint(self, ctx:marzoParser.PrintContext):
        print("syscall")
        print(" ")

    #END
    def exitEndStatement(self, ctx: marzoParser.EndStatementContext):
        print("Finishing Program ...")