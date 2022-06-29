import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

page = requests.get("https://www.nike.com.br/snkrs?gclid=CjwKCAjw55-HBhAHEiwARMCszgVz2HE5pWnPdP4RiwcM066e_ByRU31wujrme1KIa-2Le9WeNUZZohoC1esQAvD_BwE#estoque", headers = headers)

#print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

#atributos = {'class':'produto__detalhe'}
produtos_estoque = soup.find_all("h2",class_="produto__detalhe-titulo")
#site = soup.find_all('a').find('href').next_element
#link_produtos = soup.find_all("div",class_="produto__hover")[0]

#realiza busca de todos os itens
for produtos_estoque in produtos_estoque:
    print(produtos_estoque.text)
    print(produtos_estoque.get('href'))




#span = class="DFlfde SwHCTb"
##quantidade_total_pares = soup.find_all("h4",class_="product-title")
#item = soup.find_all("h4",class_=" product-title")[0]
#print(valor_dolar) //printa valor e text with span
#print(valor_dolar.text)
#print(respostas.text)
#print(item)