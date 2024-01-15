.MODEL SMALL
 
.STACK 100H

.DATA 

    len DW 3;               ; will len to take input,iterate string
    string DB 256 dup('$')  ; hold the input chars(max=100)
    
    prompt_unique DB "UNIQUE INPUT$"
    prompt_not_unique DB "NOT UNIQUE INPUT$"
.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

; -- code here --


; (1) lets reda the len
mov cx, [len]   ; okey

; (2) let input the word

mov ah,1
mov si, 0
input_word:
    int 21h ; takes the input
    mov string[si], al
    inc si
loop input_word

; (3) lets print the string
lea dx, string
mov ah, 9
int 21h

; (4) lets push all the chars to stack 
mov cx, [len]
mov si, 0
push_to_stack:        
    mov ah, 0           ; cuz  size of each block in stack - 16bit
    mov al, string[si]
    push ax
    inc si
loop push_to_stack 

; (5) lets pop all the chars from stack
mov cx, [len]

pop_from_stack:        
    pop ax
    
    ; now, lets iterate 0 - (cx-1) and if poped value exist in this 
    ; range, then not unique, else continue till last first pushed
    ; char
    mov si, cx
    sub si, 2      ; ** need to iterate from rev order **
    inner_loop:
        ; break if si < 0
        mov dx, 0
        cmp si,dx
        jl end_inner_loop
        
        ; lets read value at string[si]
        mov bl,string[si]
        cmp bl,al       ; only comparing the byte that matters :)
        je not_unique   ; if equal, not unique, else continue
    
        ; must to end the loop
        dec si
    jmp inner_loop
    end_inner_loop:
loop pop_from_stack
; of not entered not_unique:  then unique
; place to print unique; 
    lea dx, prompt_unique
    mov ah, 09
    int 21h
jmp end_unique_test
not_unique:
    lea dx, prompt_not_unique
    mov ah, 09
    int 21h
end_unique_test:



;exit to DOS    
mov ah, 4Ch
int 21h
MAIN ENDP
END MAIN 
