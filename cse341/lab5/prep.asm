.MODEL SMALL
 
.STACK 100H

.DATA                

size DW 65

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here

; lets read size

mov AX,size[0]
; mov dl, al 
mov dx, ax

mov ah, 02h
int 21h





;exit to DOS    

MAIN ENDP
END MAIN 
