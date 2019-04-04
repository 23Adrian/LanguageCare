grammar care;


/*******

parser rules
***********/

prog : statements EOF;

statements : statement*;

statement : exp;

exp : exp OPERATOR exp | INT;


/*********
Lexer Rules
********/

// operators
DIV :       '/' ;
MINUS :     '-' ;
PLUS :      '+' ;
MULTIPLY :  '*' ;
EXPO :      '^' ;

OPERATOR : DIV | MULTIPLY | PLUS | MINUS | EXPO ;

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