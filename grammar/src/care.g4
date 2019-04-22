grammar care;
/*******

parser rules
***********/

prog : statements EOF;

statements : statement*;

statement : finished;

finished :
    (
    exp
    )
    SEMI;

exp :
    IF exp THEN exp ELSE exp    |
    SI exp HAGA exp SINO exp    |

    MAP LIST TO exp             |
    MAP LIST AL exp             |

    LParen exp RParen           |
    exp EXPO exp                |
    MINUS exp                   |
    exp (MULTIPLY | DIV ) exp   |
    exp (PLUS | MINUS)  exp     |
    INT
    ;


expList :       propExpList     ;
propExpList :

    exp                         |
    (exp COMMA propExpList)     ;








/*********
Lexer Rules
********/

// operators
MINUS   :     '-' ;
PLUS    :     '+' ;
MULTIPLY:     '*' ;
EXPO    :     '^' ;
DIV     :     '/' ;

EQUAL   :    '=' ;
LEQUAL  :    '<=';
MEQUAL  :    '>=';
NEQUAL  :    '!=';
AND     :    '&' ;

COMMA   :    ',' ;
LParen  :    '(' ;
RParen  :    ')' ;
SEMI    :    ';' ;




// BLANK SPACES

NEWLINE : '\r'? '\n' -> skip;
WS : (' ' | '\t')+ -> skip;

//how to comment code

LINE_COMMENT : DIV DIV ~[\r\n]* -> channel(HIDDEN);


//OTHER TOKENS


IF :     'if'       ;
SI :     'si'       ;

ELSE:    'else'     ;
SINO:   'sino'      ;

THEN:   'then'      ;
HAGA:   'haga'      ;

MAP:    'map'       ;

DEFINE: 'define'    ;
DIAGNOS:'diagnos'   ;

LIST:   'list'      ;


TO:     'to'        ;
AL:     'al'        ;








//BASE CHARACTERS

INT : DIGIT+;
STRING : LETTER+;


/******
fragments
*******/

fragment DIGIT : [0-9];

fragment LETTER : [a-z] | [A-Z] ;





