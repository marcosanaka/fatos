#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- encoding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re


# In[2]:


# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx"


# In[3]:


linkext = "https://www.rad.cvm.gov.br/ENET/"
protocolo=''
datahora=''


# In[4]:


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.implicitly_wait(10)  # in seconds
element = driver.find_element_by_xpath("//div[@id='grdDocumentos_wrapper']//table[@id='grdDocumentos']")
html_content = element.get_attribute('outerHTML')
print("OK")


# In[5]:


#print(html_content)
#utilizar a biblioteca BeautifulSoup para extrair a tabela e parsear o HTML. 
res = BeautifulSoup(html_content, 'html.parser')
#print(res)


# In[6]:


#Acessar o elemento chamando o método find passando como argumento o nome da tag, no caso table 
count=0
table = res.find(name='tbody')
filtro1 = table.find_all(name='tr')
#print(filtro1)
for tag in filtro1:
    count2=0
    filtro2 = tag.find_all('td')
    for tags in filtro2:
        count2=count2+1
        result=tags
        if count2==2:
            empresa=result.getText()
            #print(empresa)
        if count2==3:
            categoria=result.getText()
        if count2==4:
            tipo=result.getText()
        if count2==7:
            data=result.getText()
            data=data.split()
        if count2==11:
            link=str(result).split("'")
            link =linkext + link[1]
            protocolo=link.split("=")[1]
            #print(protocolo)
        #testes    
        #print(result)
        #print(count2)
        
    if protocolo : 
        if (categoria != "Formulário de Referência" and categoria != "Formulário Cadastral"):
            print(empresa)
            protocolo=re.sub('[^0-9]', '', protocolo)
            print("protocolo :"+protocolo)
            print(categoria)
            print (data[1])
            print ("hora: "+data[2])
            print(link)
            protocolo=''
            #print(count)
            print("==============================================================================================")
            count = count+1
            print(count)
if count==0:
    print("sem dados")
print("fim")


# In[417]:


driver.quit()


# In[ ]:




