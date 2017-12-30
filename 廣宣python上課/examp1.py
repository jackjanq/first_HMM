import requests
from bs4 import BeautifulSoup

def get_hotline_udnnews(url):
    resp = requests.get(url)
    
    if resp.status_code is 200:
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        scope1 = soup.select("#tab1") #����Ĥ@�Ϭq
        scope2 = scope1[0].select(".taba") #����ĤG�Ϭq
        
        hot_lines = []
        
        for line in scope2: #������@��list�A��i�^��
            hot_lines.append(line.text) 
            
        return hot_lines


if __name__ == '__main__':
    udnnews_lines = get_hotline_udnnews("https://udn.com/news/index")
    i = 0
    
    while i < len(udnnews_lines): 
        print(udnnews_lines[i])
        i += 1