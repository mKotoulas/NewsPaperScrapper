from os import makedirs
from datetime import datetime  
from openpyxl import Workbook 
from rich.progress import Progress

wb = Workbook() 

def initialize_sheet(newspaper_name): 
    avgi_sheet=wb.create_sheet(newspaper_name)  
    try:del wb['Sheet']
    except KeyError:pass  
    avgi_sheet.insert_cols(5)   
    titles=["Title","Summary","Link","Date","Time"] 
    avgi_sheet.append(titles)         

 

def save_results(results,news_name):  
    sheet=wb[news_name]
    for page in results:
        for article in page:sheet.append(article)  
    wb.save("results.xlsx")       

    





