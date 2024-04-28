
%{ 
%}
 
%% 
[ \t]     { /* skip blanks and tabs */ } 
\n|.      { return yytext[0]; }
%% 