.MODEL SMALL
 
.STACK 100H

.DATA 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here

mov ax, 20
mov bx, 10


mov cx, 0

cmp ax, 0

start_loop:
    je end_loop
    add cx, bx
    dec ax
    jmp start_loop
end_loop:




;exit to DOS    

MAIN ENDP
END MAIN 


