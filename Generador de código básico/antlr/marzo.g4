grammar marzo;
program : expression*statement* ;

expression:
    Numero                      #numero
    | Char                      #char
    | expression '+' expression #suma  
    | expression '-' expression #resta                 
    | expression '=' expression #asignacion                     
    | expression '<' expression #menor
    | expression '>' expression #mayor
    ;

statement:
    'if (' expression ') do' statement                       #if
    | 'if (' expression ') do' statement 'else do' statement #ifElse
    | 'int' Char                                             #declaracion
    | 'print(' expression ')'                                #print
    | statement ';'                                          #endStatement
    | 'int' expression                                       #asignacionExp
    ;

Numero : [0-9]+;
Char: [a-zA-Z];
Todo: [a-zA-Z0-9]+;

WS : [ \t\n\r]+ -> skip ;