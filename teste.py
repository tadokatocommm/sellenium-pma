import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Carregando os e-mails do Excel
excel_path = 'dados.xlsx'
df = pd.read_excel(excel_path)
first_email = df['Email'].iloc[0]  # Pegando o primeiro e-mail da coluna

# Configurando o Selenium
driver = webdriver.Chrome()
driver.get('https://www.google.com.br/?hl=pt-BR')
time.sleep(5)

# Localizando o campo de pesquisa do Google e inserindo o e-mail
search_box = driver.find_element(By.NAME, 'q')  # 'q' é o nome do campo de busca do Google
search_box.send_keys(first_email)  # Inserindo o e-mail no campo de busca
search_box.send_keys(Keys.RETURN)  # Pressionando Enter para pesquisar

# Aguarde alguns segundos para ver o resultado
time.sleep(5)

# Fechar o navegador (opcional)
driver.quit()
