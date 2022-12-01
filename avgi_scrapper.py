from network import get_html
from network import make_soup 
from menu_items import clear 
from time import sleep 
from rich.progress import Progress 
from rich import print 
from rich.prompt import IntPrompt
from excel_builder import initialize_sheet,save_results 

url_dictionary={ "1":"https://www.avgi.gr/politiki","2":"https://www.avgi.gr/oikonomia",
                  "3":"https://www.avgi.gr/koinonia","4":"https://www.avgi.gr/diethni", 
                  "5":"https://www.avgi.gr/tehnes","6":"https://www.avgi.gr/athlitika",
                  "7":"https://www.avgi.gr/entheta","8":"https://www.avgi.gr/gnomes"  
               }  

FLAG=True 

def take_articles_info(soupa):
    page_info=[] 
    teasers=soupa.find("div",{"class","horizontal-teasers"}) 
    articles=teasers.find_all("article",{"class":"horizontal-teaser left-back"})  
    for article in articles: 
        try:
            link=article.find("a")["href"]
            title=article.find("h4",{"class":"double-title"}).text
            date,time=article.find("time",{"class":"default-date"}).text.lstrip().rstrip().split(" ")  
            article_summary=article.find("div",{"class","teaser-summary"}).text   
            page_info.append([title,article_summary,link,date,time])
        except AttributeError:continue 
    return page_info

def avgi_scrap(avgi_choice):
    results=[]
    global FLAG
    if FLAG:
        initialize_sheet("AVGI")  
        FLAG=False     
    url=url_dictionary[avgi_choice]   
    starting_page=IntPrompt.ask("[cyan]Enter starting page(type 0 for first page)")           
    pages=IntPrompt.ask("[cyan]How many pages you want to scrape:")
    if pages==0:return             
    name=url_dictionary[avgi_choice].split("/")[-1] 
    clear()
    sleep(0.1)   
    print(f"[dark_olive_green3]Category selected:{name}")    
    print(f"[dark_olive_green3]Starting page:{starting_page}\tPages to scrap:{pages}")    
    with Progress() as progress:
        task1 = progress.add_task("[green]Downloading...", total=pages) 
        while not progress.finished: 
            for page in range(starting_page,pages): 
                sleep(0.5) 
                params={"page":page} 
                html=get_html(url,params)
                if html: 
                    soupa=make_soup(html)
                    if soupa:results.append(take_articles_info(soupa))  
                progress.update(task1, advance=1) 
                sleep(0.2) 
    save_results(results,"AVGI")           
  


 