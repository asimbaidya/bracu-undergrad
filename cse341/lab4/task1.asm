.MODEL SMALL
 
.STACK 100H

.DATA 

    nl DB 0dH, 0AH, "$"
    msg DB  "Done Printing 80 Star$"

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here

mov cx, 80
mov ah, 2
mov dl, '*'

start_loop:
    int 21h
    loop start_loop


mov ah, 9
lea dx, nl
int 21h
mov dx msg
int 21h


;exit to DOS    

MAIN ENDP
END MAIN 

