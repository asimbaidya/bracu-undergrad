code segment
start:
mov ax, data
mov ds, ax
mov es, ax



;

; output a char
mov ah, 2
mov dl, "?"
int 21h

; input a char
mov ah, 1
int 21h
mov bl, al

; go to new line
mov ah, 2
mov dl, 0dh
int 21h
mov ah, 2 ; not required ( as previously set to 2) 
mov dl, 0ah
int 21h


;display input char
mov dl, bl
int 21h


; exit to operating system
mov ah, 4ch
int 21h



