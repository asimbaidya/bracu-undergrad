
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

    mov ah, 2
    mov dl,"A"
 
    mov cx, 58 
    
    print_atoz:
    int 21h
    inc dl
    loop print_atoz

ret




