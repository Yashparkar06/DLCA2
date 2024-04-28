%{
    #include<stdio.h>
    int i;
    int yywrap();
%}

%% 
[0-9]+ {
    i=atoi(yytext);
    if(i % 2 == 0){
        printf("Even");
    }
    else{
        printf("Odd");
    }
}
%%

int yywrap(){
    return 1;
}

int main(){
    printf("Enter a number: \n");
    yylex();
    return 0;
}

// Enter a number: 
// 10
// Even
// 13
// Odd