
INCLUDE 'EMU8086.INC'

.MODEL SMALL
 
.STACK 100H

.DATA                     
; here "x" means x is ascii representation char, not exact decimal/hex value   
; remember; 65 is valid byte, thus 'A'
; also, writing 6565 will cause error as 6565 is greater than the 8 bit cap.
; and , 'AA', will just means 65,65
array_of_byte DB "12395", 'A', 65, 65

; stop when $ is found

.CODE 
MAIN PROC 

;iniitialize data segment;
MOV AX,@DATA 
MOV DS,AX      

; len = 5
mov cx, 5
                       
PRINTN "This will print new LINE"
PRINT "This does not print new line and \n does not works", 0FH, 0DH

mov ah, 02h
print_1:

mov SI, CX
dec SI
mov dl, array_of_byte[SI];
int 21h

loop print_1 


;exit to DOS    

MAIN ENDP
END MAIN 
