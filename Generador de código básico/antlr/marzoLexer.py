# Generated from c:\Users\lalo2\OneDrive\Escritorio\8vo Semestre\Dise�o de compiladores\1er Parcial\marzo\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\6\16P\n\16\r\16\16\16Q\3\17\3\17\3\20\6\20W\n\20")
        buf.write("\r\20\16\20X\3\21\6\21\\\n\21\r\21\16\21]\3\21\3\21\2")
        buf.write("\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22\3\2\6\3\2\62;\4\2C\\c|")
        buf.write("\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2c\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2")
        buf.write("\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17\62\3\2\2\2\21")
        buf.write("\67\3\2\2\2\23?\3\2\2\2\25C\3\2\2\2\27J\3\2\2\2\31L\3")
        buf.write("\2\2\2\33O\3\2\2\2\35S\3\2\2\2\37V\3\2\2\2![\3\2\2\2#")
        buf.write("$\7-\2\2$\4\3\2\2\2%&\7/\2\2&\6\3\2\2\2\'(\7?\2\2(\b\3")
        buf.write("\2\2\2)*\7>\2\2*\n\3\2\2\2+,\7@\2\2,\f\3\2\2\2-.\7k\2")
        buf.write("\2./\7h\2\2/\60\7\"\2\2\60\61\7*\2\2\61\16\3\2\2\2\62")
        buf.write("\63\7+\2\2\63\64\7\"\2\2\64\65\7f\2\2\65\66\7q\2\2\66")
        buf.write("\20\3\2\2\2\678\7g\2\289\7n\2\29:\7u\2\2:;\7g\2\2;<\7")
        buf.write("\"\2\2<=\7f\2\2=>\7q\2\2>\22\3\2\2\2?@\7k\2\2@A\7p\2\2")
        buf.write("AB\7v\2\2B\24\3\2\2\2CD\7r\2\2DE\7t\2\2EF\7k\2\2FG\7p")
        buf.write("\2\2GH\7v\2\2HI\7*\2\2I\26\3\2\2\2JK\7+\2\2K\30\3\2\2")
        buf.write("\2LM\7=\2\2M\32\3\2\2\2NP\t\2\2\2ON\3\2\2\2PQ\3\2\2\2")
        buf.write("QO\3\2\2\2QR\3\2\2\2R\34\3\2\2\2ST\t\3\2\2T\36\3\2\2\2")
        buf.write("UW\t\4\2\2VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y \3")
        buf.write("\2\2\2Z\\\t\5\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2")
        buf.write("\2\2^_\3\2\2\2_`\b\21\2\2`\"\3\2\2\2\6\2QX]\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    Numero = 13
    Char = 14
    Todo = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'='", "'<'", "'>'", "'if ('", "') do'", "'else do'", 
            "'int'", "'print('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "Numero", "Char", "Todo", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "Numero", "Char", 
                  "Todo", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


