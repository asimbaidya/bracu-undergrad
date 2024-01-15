.MODEL SMALL
 
.STACK 100H

.DATA 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here

; byte division
mov ax, 45; 
mov bh, 20

div bh         



; word division
mov dx, 0
mov ax, 66
mov bx, 20

div bx


; simple rule:

; rem -> at high byte(of dividend)
; qut -> at low byte (of dividend)

;; in byte div - high -> ah, low -> al (high,low of dividend)
;; in word div - high -> dx, low -> ax (high,low of dividend);


;exit to DOS    

MAIN ENDP
END MAIN 
