.model small
.stack 100h


; section to declare variable
.data 
    ; db - define bytes
    var1 db 3
    var2 db ?


main proc

    ; init of data segment
    mov ax, @data
    mov ds,ax

    ;
    mov ah, 2   ; for printing
    add var1, 48 ;
    mov dl, var1
    int 21h

    ; taking input
    mov ah, 1
    int 21h
    mov var2, al


    mov ah,2
    mov dl, 10
    int 21h

    mov dl, 10
    int 21h

    mov ah, 2
    mov dl, var2
    int 21h


    exit:
    mov ah, 4
    int 21h
    main endp

end main
