import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

def executar_tarefa():

    # Carregando os e-mails do Excel
    excel_path = 'caminho/para/emails.xlsx'
    df = pd.read_excel(excel_path)
    emails = df['Email']  # Substitua 'Email' pelo nome da coluna no seu Excel

    # Configurando o Selenium
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get('https://admin.google.com/')

    # Realizando login no Google Admin
    email_field = driver.find_element(By.ID, 'identifierId')
    email_field.send_keys('seu_email_admin@gmail.com')
    email_field.send_keys(Keys.ENTER)
    time.sleep(2)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys('sua_senha')  # Substitua pela sua senha
    password_field.send_keys(Keys.ENTER)
    time.sleep(5)

    # Percorrendo os e-mails no Excel e excluindo no Admin
    for email in emails:
        search_box = driver.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]')
        search_box.clear()
        search_box.send_keys(email)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)

        try:
            delete_button = driver.find_element(By.XPATH, '//button[contains(text(), "Excluir")]')
            delete_button.click()
            time.sleep(2)

            confirm_button = driver.find_element(By.XPATH, '//button[contains(text(), "Confirmar")]')
            confirm_button.click()
            time.sleep(3)
        except Exception as e:
            print(f"Erro ao processar o e-mail {email}: {e}")

    driver.quit()

if __name__ == "__main__":
    print("Bem-vindo ao automatizador de exclusão de e-mails do Google Admin!")
    input("Pressione Enter para iniciar o processo...")
    executar_tarefa()
    print("Tarefa concluída com sucesso!")
