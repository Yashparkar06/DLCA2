%{
#include<stdio.h>
int yywrap();
%}

%%
if|else|while|return  {printf("Keyword: %s\n", yytext);}
^[a-zA-Z][a-zA-Z0-9]* {printf("Valid identifier: %s\n", yytext);}
^[^a-zA-Z] {printf("Invalid identifier: %s\n", yytext);}
%%

int yywrap(){
    return 1;
}

int main(){
    printf("Enter an identifier or keyword: \n");
    yylex();
    return 0;
}

// Enter an identifier or keyword: 
// while
// Keyword: while

// var
// Valid identifier: var

// 99var
// Invalid identifier: 99var