import requests
from bs4 import BeautifulSoup

def get_hotline_udnnews(url):
    resp = requests.get(url)
    
    if resp.status_code is 200:
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        scope1 = soup.select("#tab1") #選取第一區段
        scope2 = scope1[0].select(".taba") #選取第二區段
        
        hot_lines = []
        
        for line in scope2: #集成於一個list，後可回傳
            hot_lines.append(line.text) 
            
        return hot_lines


if __name__ == '__main__':
    udnnews_lines = get_hotline_udnnews("https://udn.com/news/index")
    i = 0
    
    while i < len(udnnews_lines): 
        print(udnnews_lines[i])
        i += 1