%option noyywrap

%{

#include"symbol_info.h"

#define YYSTYPE symbol_info*

#include "y.tab.h"

extern YYSTYPE yylval;

void yyerror(char *);

string loglist;

extern int lines;

extern ofstream outlog;

%}

delim	 [ \t\v\r\f]
newline  \r?\n
ws		 {delim}+
letter_	 [A-Za-z_]
digit	 [0-9]
id		 {letter_}({letter_}|{digit})*
integers {digit}+
floats	 {digit}*(\.{digit}+)|{digit}*(\.{digit}+)?((E|e)[-]?{digit}+)

%%

{ws}		{ /* ignore whitespace */ }
{newline}	{ lines++;
}

if          {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return IF;
}
else		{
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return ELSE;
}
for         {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return FOR;
}
while       {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return WHILE;
}
do          {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return DO;
}
break       {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return BREAK;
}
continue    {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return CONTINUE;
}
return      {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return RETURN;
}
int         {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return INT;
}
float       {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return FLOAT;
}
char        {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return CHAR;
}
void        {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return VOID;
}
double      {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return DOUBLE;
}
switch      {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return SWITCH;
}
case        {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return CASE;
}
default     {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return DEFAULT;
}
printf      {
                symbol_info *s = new symbol_info((string)yytext,":(");
                yylval = (YYSTYPE)s;
                return PRINTLN;
}

"+"|"-"	    {
                symbol_info *s = new symbol_info((string)yytext,"ADDOP");
                yylval = (YYSTYPE)s;
                return ADDOP;
		    }
"*"|"/"|"%"    {
                symbol_info *s = new symbol_info((string)yytext,"MULOP");
                yylval = (YYSTYPE)s;
                return MULOP;
            }
"++"        {
                symbol_info *s = new symbol_info((string)yytext,"INCOP");
                yylval = (YYSTYPE)s;
                return INCOP;
}
"--"        {
                symbol_info *s = new symbol_info((string)yytext,"DECOP");
                yylval = (YYSTYPE)s;
                return DECOP;
}
"<"|">"|"<="|">="|"=="|"!=" {
                symbol_info *s = new symbol_info((string)yytext,"RELOP");
                yylval = (YYSTYPE)s;
                return RELOP;
            }

"="         {
                symbol_info *s = new symbol_info((string)yytext,"ASSIGNOP");
                yylval = (YYSTYPE)s;
                return ASSIGNOP;
}
"&&"|"||"   {
		   	symbol_info *s = new symbol_info((string)yytext,"LOGICOP");
			yylval = (YYSTYPE)s;
			return LOGICOP;
		    }

"!"        {
                symbol_info *s = new symbol_info((string)yytext,"NOT");
                yylval = (YYSTYPE)s;
                return NOT;
}
"("        {
                symbol_info *s = new symbol_info((string)yytext,"LPAREN");
                yylval = (YYSTYPE)s;
                return LPAREN;
}
")"        {
                symbol_info *s = new symbol_info((string)yytext,"RPAREN");
                yylval = (YYSTYPE)s;
                return RPAREN;
}
"{"        {
                symbol_info *s = new symbol_info((string)yytext,"LCURL");
                yylval = (YYSTYPE)s;
                return LCURL;
}
"}"        {
                symbol_info *s = new symbol_info((string)yytext,"RCURL");
                yylval = (YYSTYPE)s;
                return RCURL;
}
"["        {
                symbol_info *s = new symbol_info((string)yytext,"LTHIRD");
                yylval = (YYSTYPE)s;
                return LTHIRD;
}
"]"        {
                symbol_info *s = new symbol_info((string)yytext,"RTHIRD");
                yylval = (YYSTYPE)s;
                return RTHIRD;
}
";"        {
                symbol_info *s = new symbol_info((string)yytext,"SEMICOLON");
                yylval = (YYSTYPE)s;
                return SEMICOLON;
}
","        {
                symbol_info *s = new symbol_info((string)yytext,"COMMA");
                yylval = (YYSTYPE)s;
                return COMMA;
}

{id}       {
                symbol_info *s = new symbol_info((string)yytext,"ID");
                yylval = (YYSTYPE)s;
                return ID;
            }
{integers} {
                symbol_info *s = new symbol_info((string)yytext,"INT");
                yylval = (YYSTYPE)s;
                return CONST_INT;
            }
{floats}   {
                symbol_info *s = new symbol_info((string)yytext,"FLOAT");
                yylval = (YYSTYPE)s;
                return CONST_FLOAT;
            }
