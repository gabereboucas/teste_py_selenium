import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

page = requests.get("https://www.santhaterra.com.br/produtos", headers = headers)
#print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

atributos = {'class':'product-title'}
respostas = soup.find_all("h4",attrs = atributos)

#realiza busca de todos os itens
for respostas in respostas:
    print(respostas) 
#span = class="DFlfde SwHCTb"
##quantidade_total_pares = soup.find_all("h4",class_="product-title")
#item = soup.find_all("h4",class_=" product-title")[0]
#print(valor_dolar) //printa valor e text with span
#print(valor_dolar.text)
#print(respostas.text)
#print(item)