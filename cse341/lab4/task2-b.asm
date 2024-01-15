.MODEL SMALL
 
.STACK 100H

.DATA 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here

mov cx, 100
mov ax, 0


start_loop:
    cmp cx, 5
    jl end_loop

    add ax, cx
    sub cx, 5

    jmp start_loop
end_loop:






;exit to DOS    

MAIN ENDP
END MAIN

