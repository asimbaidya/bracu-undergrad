.MODEL SMALL
 
.STACK 100H

.DATA 

FUCK DB "HELLO MOTHER FUCKER$"

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

; Macro here
PRINT MACRO str
    push dx
    push ax
    
    lea dx, str
    mov ah, 9
    int 21h
    
    pop ax
    pop dx
ENDM
;Code here
mov dh, 0ffh

PRINT FUCK
PRINT FUCK
PRINT FUCK
PRINT FUCK
PRINT FUCK




;exit to DOS    

MAIN ENDP




END MAIN  



