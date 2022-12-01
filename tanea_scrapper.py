from network import get_html
from network import make_soup 
from menu_items import clear 
from time import sleep 
from rich.progress import Progress 
from rich import print 
from rich.prompt import IntPrompt 
from excel_builder import initialize_sheet,save_results  
import re 

url_dictionary={ "1":"https://www.tanea.gr/allnews/","2":"https://www.tanea.gr/category/greece/education",
                  "3":"https://www.tanea.gr/category/greece/law/","4":"https://www.tanea.gr/category/greece/astynomika/", 
                  "5":"https://www.tanea.gr/category/greece/employment/","6":"https://www.tanea.gr/category/politics/parliament/",
                  "7":"https://www.tanea.gr/category/politics/parliament/","8":"https://www.tanea.gr/category/economy/economy-greece/",
                  "9":"https://www.tanea.gr/category/economy/diethni/","10":"https://www.tanea.gr/category/economy/forologika/","11":"https://www.tanea.gr/category/world/"
               }  

FLAG=True   

def scrape_summary(link):
    response=get_html(link) 
    if response:s=make_soup(response)
    else:return None 
    if s:
        try:
            h2_tag=s.find("h2",{"class","article-summary"}) 
            return h2_tag.text.strip() 
        except AttributeError:return None
    else:return None  

def take_articles(soupa):
    page_info=[] 
    tag_regex=re.compile("archive__tiles red0 grey-bg mt_[0-9]+")  
    articles=soupa.find_all("li",{"class":tag_regex}) 
    for article in articles:
        try:
            link=article.find("a")["href"]
            main_title=article.find("a")["title"]
            try:
                before_title=article.find("span",{"class":"hyper"}).text 
            except AttributeError:before_title="" 
            title=f"{before_title}|{main_title}"  
            date,time=article.find("time")["title"].split(",")  
            summary=scrape_summary(link) 
            if not summary:continue
            page_info.append([title,summary,link,date,time])  
        except AttributeError:continue
    return page_info  


def tanea_scrap(choice):
    results=[]
    global FLAG
    if FLAG:
        initialize_sheet("TA NEA")   
        FLAG=False 
    url=url_dictionary[choice] 
    starting_page=IntPrompt.ask("[cyan]Enter starting page")                 
    pages=IntPrompt.ask("[cyan]How many pages you want to scrape") 
    if pages==0:return
    name=url_dictionary[choice].split("/")[-2]    
    clear()
    sleep(0.1)   
    print(f"[dark_olive_green3]Category selected:{name}")    
    print(f"[dark_olive_green3]Starting page:{starting_page}\tPages to scrap:{pages}") 
    with Progress() as progress:
        task1 = progress.add_task("[green]Downloading...", total=pages)  
        while not progress.finished: 
            for page in range(starting_page,pages+1): 
                sleep(0.5)   
                html=get_html(f"{url}/page/{page}") 
                if html: 
                    soupa=make_soup(html)
                    if soupa:results.append(take_articles(soupa))     
                progress.update(task1, advance=1) 
                sleep(0.2)  
        save_results(results,"TA NEA")  

