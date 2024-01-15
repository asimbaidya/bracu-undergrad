.MODEL SMALL
 
.STACK 100H

.DATA     

; byte array for taking input 
LEN DW 3, "$"               ; total number of digit
DIGIT DB 3 dup(?)           ; array to store input
NUM DW 0                    ; to store the number
DIGIT_SUM DW 0;           

Yes DB 0Ah, 0dh,  "YES$"
No DB 0Ah, 0dh, "NO$"

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      


; (1) lets take the input
mov CX, LEN ; ** review ** 
mov si, 0
read_input:
    mov ah, 01h ; for taking input
    int 21h     ; not input on al;
                          
    ; lets remove coding part by substracting 30 from input
    sub al, 030h
    
    ; store input on array
    mov DIGIT[si], al
    
    ; add the digit(al) to digit_SUM
    mov BX, DIGIT_SUM
    mov ah, 0   ; to keep safe hand
    add BX, Ax 
    ; save back the value
    mov DIGIT_SUM, BX
    ; increase si
    inc si
loop read_input


;mov cx, LEN
;mov si, 0
;test_input:

;    mov dl, DIGIT[si]
;    add dl,030h
    
;    mov ah, 2
;    int 21h
;    inc si
;loop test_input
;; okey reading success

; not make digit and store in BX,AX, for multiplication,

mov CX, LEN
dec CX
mov si, 0
make_digit:
    ; load number 
    mov ax, NUM
    
    ; load digit at si
    mov dh, 0       ; to keep clean hand
    mov dl, DIGIT[si]
    
    ; add & sotre in ax
    add ax, dx          
    
    ; multiply with 10
    mov dx, 10
    mul dx
 
    ; now again save the result into num;
    mov NUM, AX             ; ignoring high byte of mul result
    ; edge case
    inc si
loop make_digit
; now simply add last value to num
; load num to ax
mov ax, NUM
; load last digit
mov dh, 0       ; to keep clean hand
mov dl, DIGIT[si]
add Ax, DX      ; hold the full number 

; Ax - FULL NUMBER;


; again lets load digit_SUM
mov BX, DIGIT_SUM 


; now theck if the numb % digit_sum = 0;
div bl  ; low byte is matter here ;)

; how if ah is zero, then divisible, elsea not

mov bh, 0
cmp ah, bh
je divisible
jmp not_divisible

divisible:
    ; 
    lea dx, Yes
    mov ah, 9
    int 21h
    jmp check_end
not_divisible:
    lea dx, No
    mov ah, 9
    int 21h   
check_end:


;exit to DOS    

MAIN ENDP
END MAIN
; time took - 36minutes
