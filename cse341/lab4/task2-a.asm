.MODEL SMALL
 
.STACK 100H

.DATA 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here

mov cx, 1
mov ax, 0


start_loop:
    cmp cx, 148
    jg end_loop

    add ax, cx
    add cx, 3

    jmp start_loop
end_loop:






;exit to DOS    

MAIN ENDP
END MAIN

