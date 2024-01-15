.model small


; stack size
.stack 100h


.data

    var1 db "Hello world \n\n\n$",10

.code

main proc
    
    ; 1 - single key input
    ; 2 - single key output
    ; 9 - character string output


    mov ax, @data
    mov ds, ax


    mov ah, 9    ; character string output
    lea dx, var1  ; load effective address
    int 21h       ; inturrept
                                     


    mov ah, 9    ; character string output
    lea dx, var1  ; load effective address
    int 21h       ; inturrept