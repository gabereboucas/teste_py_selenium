from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

#opts = Options()
#opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.nike.com.br/air-max-90-153-169-211-330203')

tamanho = driver.find_element_by_xpath('//*[@id="variacoes"]/div/ul/li[13]/label') 
tamanho.click() 

clicklogin = driver.find_element_by_xpath('//*[@id="anchor-acessar-unite-oauth2"]')
clicklogin.click() 

email = driver.find_element_by_xpath('//input[@type="email"]')
email.click()
email.send_keys('lll@gmail.com') 