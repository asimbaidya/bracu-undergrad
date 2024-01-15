.MODEL SMALL
 
.STACK 100H
.DATA 
    input_prompt db "Enter 3 Digit: Char: $"
    even_prompt DB " Which is Even!", 0DH, 0AH, "$"
    odd_prompt DB " Which is Odd!", 0DH, 0AH, "$"
    nl DB 0DH,0AH,"$" ; for printing new line
.CODE 
MAIN PROC 
;iniitialize DS
    MOV AX,@DATA 
    MOV DS,AX      
    ; shwoing input prompt
    LEA DX,input_prompt
    MOV AH,09H
    INT 21H
    ; now taking 3 char input into bh,bl,ch
    mov ah, 01h
    
    ; interrupt and move input to bh
    int 21h
    mov bh, al
    ; interrupt and move input to bl
    int 21h
    mov bl, al
    ; interrupt and move input to ch
    int 21h
    mov ch, al
    ; printing new line
    LEA DX,nl
    MOV AH,09H
    INT 21H
    ; TEST: lets print all to check if okey
    ; mov ah, 02h
    ; mov dl, bh
    ; int 021h
    ; mov dl, bl
    ; int 021h
    ; mov dl, ch
    ; int 021h
    ; now, lets compare bh & bl & move height value to bh
    cmp bh,bl
    jl move_bl_to_bh ; if bh < bl ; move the value
    jmp end_case_1 ; **important**
    move_bl_to_bh:
        mov bh, bl
    end_case_1:
    ; now again, compare ch to bh & move height value to bh
    cmp bh,ch
    jl move_ch_to_bh ; if bh < ch ; move the value
    jmp end_case_2 ; **important**
    move_ch_to_bh:
        mov bh, ch
    end_case_2:
    ; now lets print bh, it should be height digit
    mov ah, 02
    mov dl, bh
    int 021h
    ; part 1 Complete
    ; now check if bh is even or odd
    ; to check this, lets divide ch by 2 and after that remainder will be in ah
    ; so, we will check if ah zero, if zero -> even,  else odd
    ; simple byte  division
    mov ah, 0
    mov al, bh
    mov bh, 2
    div bh 
    ; compare and check if ah zero,
    cmp ah, 0
    je even_hain
    jmp odd_hain
    
    even_hain:
    LEA DX,even_prompt
    MOV AH,09H
    INT 21H
    jmp end_of_program ; **important**
    
    odd_hain:
    LEA DX,odd_prompt
    MOV AH,09H
    INT 21H
    jmp end_of_program ; **important**
    
    end_of_program: 
;exit to DOS    
MAIN ENDP
END MAIN 
