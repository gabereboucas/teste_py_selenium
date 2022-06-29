link_produtos = soup.find_all('a',class_='btn','href', href=True)

for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])


for produtos_estoque in soup.find_all('a'):
    print(link.get('href'))