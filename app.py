import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Carregando os e-mails do Excel
excel_path = 'dados.xlsx'
df = pd.read_excel(excel_path)
emails = df['Email'] 

# Configurando o Selenium
driver = webdriver.Chrome()
driver.get('https://admin.google.com/?hl=pt-br')
time.sleep(5)
