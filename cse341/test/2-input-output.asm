; @aan

.model small

.stack 100h


.code 


main proc

    # input 2
    mov ah, 1
    int 21h
    mov bl, al


    # input 1
    mov ah, 1
    int 21h
    mov bh, al

    
    # 2 - display
    mov ah, 2
    mov dl,bl
    int 21h

    mov ah, 2
    mov dl,bh
    int 21h


;     mov ah, 4ch
;     int 21h
;     main endp
end main
