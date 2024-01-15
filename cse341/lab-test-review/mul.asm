.MODEL SMALL
 
.STACK 100H

.DATA 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here


; byte multiplication

; for a*b => a must be in al, or ax;
; and no overflow can occur ?probably
mov al, 0ffh
mov bh, 0ffh

mul bh ; => result in ax  


; for word multiplication
; a*b => a must be in ax & result will be in DX:AX

mov ax, 0ffffh
mov bx, 0ffffh
mul bx



;exit to DOS    

MAIN ENDP
END MAIN
