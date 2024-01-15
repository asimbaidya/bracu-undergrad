#!/bin/bash

yacc -d -y --debug --verbose 20301239.y
echo 'Generated the parser C file as well the header file'
g++ -w -c -o y.o y.tab.c
echo 'Generated the parser object file'
flex 20301239.l
echo 'Generated the scanner C file'
g++ -fpermissive -w -c -o l.o lex.yy.c
# if the above command doesn't work try g++ -fpermissive -w -c -o l.o lex.yy.c
echo 'Generated the scanner object file'
g++ y.o l.o

# clean
rm -rf lex.yy.c
rm -rf l.o
rm -rf y.o
rm -rf y.tab.c
rm -rf y.tab.h

echo 'All ready, running'
./a.out input.txt
