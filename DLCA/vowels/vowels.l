%{
    int vow_count=0;
    int const_count =0;
%}

%%
[aeiouAEIOU] { vow_count++; }
[a-zA-Z]     { const_count++; }
\n           { printf("Number of vowels: %d\n", vow_count);
               printf("Number of consonants: %d\n", const_count);
               vow_count = 0;
               const_count = 0;
             }
%%
int yywrap(){}

int main()
{
    printf("Enter the string of vowels and consonants: ");
    yylex();
    // printf("Number of vowels are: %d\n", vow_count);
    // printf("Number of consonants are: %d\n", const_count);
    return 0;
}