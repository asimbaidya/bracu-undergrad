.MODEL SMALL

.STACK 100H

.DATA

.CODE
MAIN PROC

;iniitialize DS

MOV AX,@DATA
MOV DS,AX

;Code here

mov cx, 5

mov ah, 1
start_reading:
int 21h
loop start_reading

; carriage return ???
mov ah, 2
mov dl, 0dh
int 21h

; printing(ah is 02 still)
mov cx, 5
start_writing:
mov dl, '*'
int 21h
loop start_writing





;exit to DOS

MAIN ENDP
END MAIN


