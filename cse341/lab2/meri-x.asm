; using small model
.MODEL SMALL
 

; stack size
.STACK 100H


.DATA 

    msg DB "Hello World",0DH,0AH,"$"


.CODE 
MAIN PROC 

    MOV AX,@DATA 
    MOV DS,AX      
    
    
    
    ; print msg to console
    LEA DX,msg
    MOV AH,09H
    INT 21H
    
    
    
    
    ; exit from program
    MOV AH,4CH
    INT 21H

MAIN ENDP
END MAIN 
