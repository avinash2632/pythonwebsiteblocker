

import PySimpleGUI as sg
import time
from datetime import datetime as dt

hostspath=r"C:\Windows\System32\drivers\etc\hosts.txt"
 
sg.theme('DarkAmber')  
layout = [ 
        [sg.Text('Enter the value',justification='right')],
        [sg.Input()],
        [sg.Button('Enter')]
     ]






window = sg.Window('My new window', layout, size=(500,300), grab_anywhere=True)

while True:
    
     
    event, value = window.read()
    
    
    
            
    
    if event == sg.WIN_CLOSED or event == 'Enter':
        break;
        
    

blockedsite=value
print(blockedsite[0])


redirect="127.0.0.1"

while True:
    
    with open(hostspath,'r+') as file:
        
        content = file.read()
        if blockedsite[0] in blockedsite:
            pass
        else:
            
            file.write(redirect+" "+blockedsite[0]+"\n")
            break        
        
            
            
        
           
             
    
    
    
    
      
    
time.sleep(5)        
                
            
        
       
       
              
  
        
           
                          
   




