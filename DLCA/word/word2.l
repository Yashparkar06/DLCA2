%{
    #include<string.h>
    int counter = 0;
    int yywrap();
%}


%%
[ \t\n]+    {}
[a-zA-Z]+  { 
    if(strlen(yytext) > counter)
        counter = strlen(yytext); 
}
.     {}
%%

int yywrap(){
    return 1;
}

int main() {
    printf("Enter text: ");
    yylex();
    printf("Longest string length: %d\n", counter);
    return 0;
}

// Enter text: hellp world wazzzzup im abc herer ot help
// Longest string length: 8
