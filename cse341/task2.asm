.MODEL SMALL
 
.STACK 100H

.DATA 

    LEN DW 6

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here

mov CX, LEN

read_input: 
    mov ah, 1 ; to take input
    int 21h                   
    
    mov ah, 0
    push Ax

loop read_input  
 

; lets print a new line
mov ah, 2
mov dl, 0ah
int 21h 
mov dl, 0dh
int 21h      
               
               
mov CX, LEN
write_caps:
    pop ax
    
    ; caps are less than 5b
    mov bx, 05bh
    cmp ax, bx
    
    jl print
    jmp continue
    print:       
        mov ah, 2
        mov dl, al
        int 21h
    continue:
loop write_caps






;exit to DOS    

MAIN ENDP
END MAIN

;; took 10m