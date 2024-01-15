.MODEL SMALL
 
.STACK 100H

.DATA           

buff DB 5 dup(?) ; buff of size 10  
buff_true DB "Input was palindrom $"
buff_false DB "Input was not palindrom $"

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here             
             
; (1) reading input
mov cx, 5
mov si, 0
read_words:

    ; read & store to array
    mov ah,1
    int 21h
    mov buff[si], al
    
    ; increment index
    inc si  
loop read_words

; (2) writing input from array
mov cx, 5
mov si, 0
write_words:

    mov dl,buff[si]
    mov ah, 2
    int 21h          

    ; increment index
    inc si 
loop write_words

; (3) pushign to stack
mov cx, 5
mov si, 0
push_to_stack:

    mov ah, 0
    mov al,buff[si]
    push ax
    ; increment index
    inc si 
loop push_to_stack 


;; (4) read from stack
;mov cx, 5
;print_from_stack:
;
;    pop dx
;    mov ah, 2
;    int 21h
;loop print_from_stack  

;----
; print new line
mov ah,2
mov dl, 0ah
int 21h
mov dl, 0dh
int 21h 
;----

; (5) check if palindrom;
; bh will indicate if a number if palindrom.
; bh = 0; palindrom;
mov bh, 0 ; assume palindrom;
mov cx, 5
mov si, 0
palindrom_check:
    mov bl, buff[si] 
    
    ; -- output
    mov ah, 02
    mov dl,bl
    int 21h
    ; -- output
    pop dx
               
    ; -- output
    mov ah, 02
    int 21h
    ; -- output
    
    cmp bl,dl
    jne mark_false
    jmp end_mark
    mark_false:
        mov bh, 1 ; 1 indicate not a palindrom
    end_mark:
    ; increase si
    inc si
loop palindrom_check 

; (6) output result
       
mov bl, 0
cmp bh,bl
je pal_true
jmp pal_false
pal_true:
    mov ah, 09
    lea dx, buff_true
    int 21h
    jmp end_game
pal_false:
    mov ah, 09
    lea dx, buff_false
    int 21h
end_game:
;exit to DOS    

MAIN ENDP
END MAIN 
