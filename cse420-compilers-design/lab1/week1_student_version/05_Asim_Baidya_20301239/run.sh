#!/usr/bin/env bash

set -e

flex main-20301239.l && echo "flex compile success"
g++ lex.yy.c && echo "g++ compile success"
./a.out input.txt && echo "run success"

# tho show output on console
cat ./20301239-token-log.txt
