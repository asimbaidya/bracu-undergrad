.MODEL SMALL
.STACK 100H
.DATA

    input_prompt DB "Enter a digit [1-9]: $"
    nl DB 0Ah, 0Dh, "$" 
    
    p DB " Is Prime $"
    not_p DB " Is not Prime$"
    e DB " && The number is Even$"
    not_e DB " && The number is Odd$"
    

.CODE
MAIN PROC

    ; INIT DB
    MOV AX, @DATA
    MOV DS, AX
    
    ; MY CODE
    mov ah, 9
    lea dx, input_prompt
    int 21h
    
    
    ; taking input
    mov ah, 1
    int 21h
    mov bh, al
    
    ; printing new line
    mov ah, 09
    lea dx, nl
    int 21h
    
    ; showing num output
    mov ah, 02
    mov dl, bh
    int 21h
    
    
    ; now bh = bh-30; 
    sub bh, 030h
    
    
    ; lets keep track of if bh was prime in bl;
    mov cl, 2
    
    
    loop_start:
        cmp cl,bh
        je loop_end ; if cl == bh ; loop end  
        
        ; if bh(input) is 1, then mark not prime and  quit loop
        cmp bh, 1
        je mark_not_priem_and_quit
        
        mov ah, 0
        mov al, bh ; out input in bh
        
        div cl
        
        cmp ah, 0 ; means divisible so not prime
        je mark_not_priem_and_quit
        jne continue
    
        mark_not_priem_and_quit:    
            mov bl, 1
            jmp loop_end
        continue:
        
        ; increasing cl
        inc cl
        jmp loop_start
    
    loop_end:
    
    ; prime check done
    
    cmp bl, 0
    je prime
    jne not_prime
    jmp end_primec_check
    
    prime:
        mov ah,09h
        lea dx, p
        int 21h
        jmp end_primec_check
    not_prime:
        mov ah, 09h
        lea dx, not_p
        int 21h
        jmp end_primec_check
    end_primec_check:
    
    
    ; odd even check now
    mov ah, 0
    mov al, bh ; out input in bh
    mov cl, 02
    div cl 
    
    cmp ah, 0
    je even
    jne not_even
    jmp end_even_check
    
    even:
        mov ah,09h
        lea dx, e
        int 21h
        jmp end_even_check
    not_even:
        mov ah, 09h
        lea dx, not_e
        int 21h
        jmp end_even_check
    end_even_check:
   
    
    
    
    ;EXIT FROM MAIN
    MAIN ENDP

END MAIN


