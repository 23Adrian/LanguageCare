grammar care;


/*******

parser rules
***********/

prog : statements EOF;

statements : statement*;

statement : finished;

finished : (exp
    ) SEMI;

exp :
    LParen exp RParen           |
    exp EXPO exp                |
    MINUS exp                   |
    exp (MULTIPLY | DIV ) exp   |
    exp (PLUS | MINUS)  exp     |
    INT;


/*********
Lexer Rules
********/

// operators
MINUS :     '-' ;
PLUS :      '+' ;
MULTIPLY :  '*' ;
EXPO :      '^' ;
DIV :       '/' ;

EQUAL :     '=' ;
LEQUAL :    '<=';
MEQUAL :    '>=';
NEQUAL :    '!=';
AND    :    '&' ;

LParen :    '(' ;
RParen :    ')' ;
SEMI   :    ';' ;


// BLANK SPACES

NEWLINE : '\r'? '\n' -> skip;
WS : (' ' | '\t')+ -> skip;

//how to comment code

LINE_COMMENT : DIV DIV ~[\r\n]* -> channel(HIDDEN);


//OTHER TOKENS

IF : 'if';
SI : 'si';




//BASE CHARACTERS

INT : DIGIT+;
STRING : LETTER+;

/******
fragments
*******/

fragment DIGIT : [0-9];

fragment LETTER : [a-z] | [A-Z] ;





