%{ 
   #include <ctype.h> 
   #include <stdio.h> 
   #define YYSTYPE double /* double type for yacc stack */ 
%} 
 
%%
 Lines :  Lines S '\n' { printf("OK \n"); }
       |  S '\n’
       |  error '\n' {yyerror("Error: reenter last line:");
                        yyerrok; };
 S     :  '(' S ')’
       |  '[' S ']’
       |   /* empty */    ;
%% 
 
#include "lex.yy.c" 
  
void yyerror(char * s)
/* yacc error handler */
{   
 fprintf (stderr, "%s\n", s);
} 
  
int main(void) 
 {
 return yyparse();
 }  