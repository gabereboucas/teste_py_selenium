import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

page = requests.get("https://www.nike.com.br/snkrs?gclid=CjwKCAjw55-HBhAHEiwARMCszgVz2HE5pWnPdP4RiwcM066e_ByRU31wujrme1KIa-2Le9WeNUZZohoC1esQAvD_BwE#estoque", headers = headers)

soup = BeautifulSoup(page.content,'html.parser')

produtos_estoque = soup.find_all("h2",class_="produto__detalhe-titulo")

link_produtos = soup.find_all("a",class_="btn",href=True)

for produtos_estoque in produtos_estoque: 
    for link_produtos in link_produtos:
        print(link_produtos['href'])
print(produtos_estoque.text)


    
    


