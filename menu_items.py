from console import console
from rich import print 
from rich.table import Table
from os import get_terminal_size,system 
 
def clear(): system("cls") 

def main_table():  
    title="[dark_olive_green3]Welcome to NewsScrapper\nA python script to scrape data from greek newspapers"
    caption="[white on red]Happy Scrapping!"
    width=width=round(get_terminal_size().columns*0.8)
    table= Table(title=title,caption=caption,width=width)   
    table.add_column("[orange3]Choice", justify="center", style="cyan")     
    table.add_column("[green_yellow]Site",justify="center",style="magenta")
    table.add_column("[orange3]Homepage Link",justify="center",style="cyan")   
    table.add_row("1", "AVGI","[link]https://www.avgi.gr/")  
    table.add_row("2", "TA NEA","[link]https://www.tanea.gr/")      
    table.add_row("3", "EXIT","-")     
    console.print(table)  

def avgi_table(): 
    title="[dark_olive_green3]AVGI Main Menu"
    width=width=round(get_terminal_size().columns*0.8)
    table=Table(title=title,width=width)  
    table.add_column("[orange3]Choice[/orange3]", justify="center", style="cyan") 
    table.add_column("[green_yellow]Topic[/green_yellow]",justify="center",style="magenta") 
    table.add_row("1", "Politics") 
    table.add_row("2", "Economy")
    table.add_row("3", "Society")
    table.add_row("4", "International")
    table.add_row("5", "Art") 
    table.add_row("6", "Sports")
    table.add_row("7", "More")
    table.add_row("8", "Opinions")
    table.add_row("9", "Main Menu")  
    table.add_row("10", "Exit script") 
    console.print(table)   

def tanea_table(): 
    title="[dark_olive_green3]TANEA Main Menu"
    width=width=round(get_terminal_size().columns*0.8)
    table=Table(title=title,width=width)  
    table.add_column("[orange3]Choice[/orange3]", justify="center", style="cyan") 
    table.add_column("[green_yellow]Topic[/green_yellow]",justify="center",style="magenta") 
    table.add_row("1", "News") 
    table.add_row("2", "Greece-->Education")
    table.add_row("3", "Greece-->Law") 
    table.add_row("4", "Greece-->Justice") 
    table.add_row("5", "Greece-->Employment")   
    table.add_row("6", "Politics-->Parliament")
    table.add_row("7", "Politics-->Goverment")    
    table.add_row("8", "Economy-->Greece")  
    table.add_row("9", "Economy-->International")  
    table.add_row("10", "Economy-->Tax news")    
    table.add_row("11", "World")  
    table.add_row("12", "Main Menu") 
    table.add_row("13", "Exit") 
    console.print(table) 
    

