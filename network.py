from requests import get
from requests.exceptions import RequestException  
from bs4 import BeautifulSoup as soup   
from contextlib import closing 

def is_good_connection(resp):
    content_type=resp.headers["Content-Type"].lower() 
    return (resp.status_code==200 and content_type is not None)

def get_html(url,params={}):  
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}   
    try:
        with closing(get(url,headers=headers,params=params)) as resp:  
            if is_good_connection(resp): return resp.content 
            else: return None 
    except RequestException as e:
        print(f"Error in {url}:{e}") 
        return None  

def make_soup(html):
    if html: return soup(html,"lxml")   
    else: return None 