# takint input

```asm
.MODEL SMALL

.STACK 100H

.DATA

    prompt db "Enter A Char: $"
    eng_msg db "Done$"

.CODE
MAIN PROC

    ;iniitialize DS
    MOV AX,@DATA
    MOV DS,AX

    ;Code here

    ; prompt
    lea dx, prompt
    mov ah, 9
    int 21h

    ; taking input char
    mov ah, 1
    int 21h
    mov bl,al

    ; new line print
    mov ah, 2
    mov dl, 0Ah
    int 21h
    mov dl, 0Dh
    int 21h



    mov dl, bl
    int 21h

    ; new line print
    mov ah, 2
    mov dl, 0Ah
    int 21h
    mov dl, 0Dh
    int 21h

    lea dx, eng_msg
    mov ah, 9
    int 21h



    ;exit to DOS
    mov ah, 4ch
    int 21h

MAIN ENDP
END MAIN

```
