from menu_items import clear,main_table,avgi_table,tanea_table
from avgi_scrapper import avgi_scrap
from tanea_scrapper import tanea_scrap
from rich.prompt import Prompt
from sys import exit  
from time import sleep    


SITES=3 
AVGI_OPTIONS=10
TANEAOTIONS=9 

def avgi_menu():
    avgi_table() 
    choice=Prompt.ask("[cyan]Select",choices=[str(i) for i in range(1,AVGI_OPTIONS+1)])        
    sleep(0.3) 
    if choice=="9":
        clear() 
        sleep(0.1) 
        menu_run() 
    elif choice=="10": 
        clear()  
        exit() 
    else:
        clear() 
        sleep(0.1)
        avgi_scrap(choice)   
        clear()
        sleep(0.1)
        menu_run()

def tanea_menu():
    tanea_table()  
    choice=Prompt.ask("[cyan]Select",choices=[str(i) for i in range(1,TANEAOTIONS+1)])         
    sleep(0.3) 
    if choice=="12":
        clear() 
        sleep(0.1) 
        menu_run() 
    elif choice=="13":   
        clear()  
        exit() 
    else:
        clear() 
        sleep(0.1)
        tanea_scrap(choice)      
        clear()
        sleep(0.1)
        menu_run()  

SUBMENUS={"1":avgi_menu,"2":tanea_menu,"3":exit} #Modify dictionary if another site added   

def menu_run():
    main_table()  
    choice=Prompt.ask("[cyan]Select",choices=[str(i) for i in range(1,SITES+1)]) 
    clear()
    sleep(0.1) 
    SUBMENUS[choice]()   

 
 
    

