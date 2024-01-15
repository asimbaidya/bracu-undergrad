.MODEL SMALL
 
.STACK 100H

.DATA 
    nl DB "|",0AH, 0Dh, "$"

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX      

;Code here


; let use bx for keeping track of ascii
mov bh, 080h
mov bl, 0ffh
start_outer_loop:
    cmp bh, bl ; comparison need to be done in here
    jg end_outer ; end loop when => bh > ff == true



    ;  now inner loop
    mov cx, 10
    inner_loop:
        cmp bh, bl
        jg end_inner

        ; now lets print the char
        mov ah, 02
        mov dl, bh
        int 21h

        ; inc must happen in inner loop
        inc bh

        loop inner_loop
    end_inner:

    ; lets print new char
    mov ah, 9
    lea dx, nl
    int 21h

    jmp start_outer_loop
end_outer:



;exit to DOS    

MAIN ENDP
END MAIN 
