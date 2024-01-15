%option noyywrap

%{

#include<bits/stdc++.h>
using namespace std;

ofstream yyoutlog; //output filestream for log file

string loglist = ""; //list of tokens along with line numbers

// define necessary c++ variables and functions here (if any)
int lines=1; //to keep track of line numbers


// function to make dirty work in a tidy fashion

void tidy_logger(string token, string lexeme, int line){
    loglist="Line no "+to_string(line)+": Token <"+token+"> Lexeme "+lexeme+" found"+"\n"+"\n";
    yyoutlog<<loglist;
}

%}

/* Regular Definitions */
/* delim [ \t\n]*/

/* write regular expressions for whitespace and newline */
ws [ ]
newline  [\n]

letter [a-zA-Z]
digit [0-9]
underscore [_]

/* write regular expressions for id, float and integers */

id ({letter}|{underscore})({letter}|{digit}|{underscore})*
integer {digit}+
float ({digit}+"."{digit}+)|("."{digit}+)

/* --------------------new task--------------------  */
/* no comment allowed in next section(but allowed in tho{}) */

%%

{ws} {  
    /* ignore whitespace */
}

{newline} { 
    /* on finding newline, increment line number*/
    lines++ ;
}

{integer} {
    tidy_logger("CONST_INT", yytext, lines);
}

{float} {
    tidy_logger("CONST_FLOAT", yytext, lines);
}

if {
    tidy_logger("IF", yytext, lines);
}
else {
    tidy_logger("ELSE", yytext, lines);
}
for {
    tidy_logger("FOR", yytext, lines);
}
range {
    tidy_logger("RANGE", yytext, lines);
}
break {
    tidy_logger("BREAK", yytext, lines);
}
not {
    tidy_logger("NOT", yytext, lines);
}
catch {
    tidy_logger("CATCH", yytext, lines);
}
try {
    tidy_logger("TRY", yytext, lines);
}
except {
    tidy_logger("EXCEPT", yytext, lines);
}
True {
    tidy_logger("TRUE", yytext, lines);
}
False {
    tidy_logger("FALSE", yytext, lines);
}
def {
    tidy_logger("DEF", yytext, lines);
}
return {
    tidy_logger("RETURN", yytext, lines);
}
finally {
    tidy_logger("FINALLY", yytext, lines);
}
and {
    tidy_logger("AND", yytext, lines);
}
or {
    tidy_logger("OR", yytext, lines);
}
print {
    tidy_logger("PRINT", yytext, lines);
}
in {
    tidy_logger("IN", yytext, lines);
}
continue {
    tidy_logger("CONTINUE", yytext, lines);
}
pass {
    tidy_logger("PASS", yytext, lines);
}
None {
    tidy_logger("NONE", yytext, lines);
}

"+"|"-" {
    tidy_logger("ADDOP", yytext, lines);
}
"++"|"--" {
    tidy_logger("INCOP", yytext, lines);
}
"<"|">"|"==" {
    tidy_logger("RELOP", yytext, lines);
}
"=" {
    tidy_logger("ASSIGNOP", yytext, lines);
}
"&&"|"||" {
    tidy_logger("LOGICOP", yytext, lines);
}
"!" {
    tidy_logger("NOT", yytext, lines);
}
"(" {
    tidy_logger("LPAREN", yytext, lines);
}
")" {
    tidy_logger("RPAREN", yytext, lines);
}
"{" {
    tidy_logger("LCURL", yytext, lines);
}
"}" {
    tidy_logger("RCURL", yytext, lines);
}
"[" {
    tidy_logger("LTHIRD", yytext, lines);
}
"]" {
    tidy_logger("RTHIRD", yytext, lines);
}
"," {
    tidy_logger("COMMA", yytext, lines);
}
":" {
    tidy_logger("COLON", yytext, lines);
}

{id} {
    tidy_logger("ID", yytext, lines);
}


%%

int main(int argc, char *argv[])
{


	if(argc != 2) 
	{
        cout<<"Please input file name"<<endl;
        cout<<"usage: ./a.out <input_file_name>"<<endl;
		return 0;
	}

    // the file to be read must be assigned to yyin
	yyin = fopen(argv[1], "r");

	if(yyin == NULL) // file does not exist
	{
        cout<<"File does not exist"<<endl;
	}

    // remember to rename the log file as mentioned in the spec
	yyoutlog.open("20301239-token-log.txt", ios::trunc); 
	

    // start reading the input file in a loop
    //💥💥
	yylex(); 
    //💥💥
	
	//print total number of lines found in the input file
    yyoutlog<<"\nTotal lines: "<<lines<<"\n";

    // close the log file
	yyoutlog.close();
	
    // close the input file
	fclose(yyin); 
}
