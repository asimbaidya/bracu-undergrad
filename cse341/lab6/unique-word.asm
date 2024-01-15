.MODEL SMALL
 
.STACK 100H

.DATA 

    len DW 5;               ; will len to take input,iterate string
    string DB 100 dup('$')  ; hold the input chars(max=100)
.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

; -- code here --


; (1) lets reda the len
mov cx, [len]   ; okey

; (2) let input the word

mov ah,2
mov si, 0
input_word
console.log(v());
    int 21h ; takes the input
    mov string[si], al
loop input_word






;exit to DOS    

MAIN ENDP
END MAIN 

