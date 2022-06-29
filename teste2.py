import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

page = requests.get("https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome.0.69i59j0l9.1652j1j7&sourceid=chrome&ie=UTF-8", headers = headers)
#print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

atributos = {'class':'g'}
#respostas = soup.find_all("div",attrs = atributos)
#print(respostas[0].get_text()) //printa pag inteira
#span = class="DFlfde SwHCTb"
valor_dolar = soup.find_all("span",class_="DFlfde SwHCTb")[0]

#print(valor_dolar) //printa valor e text with span
print(valor_dolar.text)
print(valor_dolar['data-value'])