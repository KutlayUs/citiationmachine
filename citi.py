

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
                
browser.get('https://www.google.com/')
browser.find_element_by_xpath("//*[@id='vc3jof']").click()
browser.find_element_by_xpath("//*[@id='tbTubd']/div/li[13]").click()
browser.find_element_by_xpath("//*[@id='L2AGLb']").click()   
srch= browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
article= input('Give a article name:')
srch.send_keys(article)
srch.send_keys(Keys.RETURN)
time.sleep(3)
try:
        srch2= browser.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/a")
        srch2.click()
except:
        srch2= browser.find_element_by_xpath("//*[@id='rso']/div[2]/div/div[1]/div/a")
        srch2.click()       
#time.sleep(1)
doi_source=browser.find_elements_by_xpath("// a[contains(text(),\
'doi')]")
try:
        print(doi_source)
        doi_text=doi_source[0].text
except:
        doi_text=doi_source[1].text
browser2 = webdriver.Chrome()
browser2.get('https://sci-hub.se/')
text= browser2.find_element_by_xpath("//*[@id='input']/form/input[2]")
text.send_keys(doi_text)
text.send_keys(Keys.RETURN)
citi1= browser2.find_element_by_xpath("//*[@id='citation']")
citi2= browser2.find_element_by_xpath("//*[@id='citation']/i")
print(f'{citi1.text},{citi2.text}')
                 
browser.close()
browser2.close()


