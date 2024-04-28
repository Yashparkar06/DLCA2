%{
    #include<stdio.h>
    int yywrap();
%}

%%
[-+*/=<>!&|^]+  {printf("operators are: %s\n",yytext);}
.
%%

int yywrap(){
    return 1;
}

int main(){
    printf("Enter an operation: ");
    yylex();
    return 0;
}


// Enter an operation: 10 + 10 - 10
// operators are: +
// operators are: -