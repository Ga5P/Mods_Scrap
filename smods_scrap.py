from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


list_nations = ['british', 'french']
dic = {}


for nation in list_nations:
    url = f'https://smods.ru/?s={nation}'
    
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    
    for element in soup.findAll('div',{'page-title hu-pad group'}):
        text = element.get_text()
        
        number = [int(s) for s in text.split() if s.isdigit()] 
        
        page_number = round(number[0] / 10)
        
    dic[nation] = page_number
    print(f' The country {nation} has {dic[nation]} pages')

dic_url = {}
for nation in dic:
    
    print(f'My key is {nation}')
    print(f'My value is {dic[nation]}')
    
    list_pages = range(1, dic[nation]+2) 

    list_pages = [f"/page/{p}" for p in list_pages]
    
    list_url = [f"https://smods.ru{p}?s={nation}" for p in list_pages]


    ''' En une ligne ---> list_url = [f"https://smods.ru/page/{p}?s={nation}" for p in range(1, dic[nation]+2)] '''
    
    infoz = []

    
    for url in list_url[:5]:
        
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content)
        
        for element in soup.findAll('div',{'class': 'post-inner post-hover'}):

            category = element.find('a').get('rel')
            title = element.find('a').get('title')
            link = element.find('a').get('href')
            author = element.find('a').get('target')
            
            info = (title, category, link, author)
            infoz.append(info)
            
    dic_url[nation] = infoz
            
            
            
test = element.copy()
