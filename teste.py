from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time 

# Caminho para o perfil do Chrome
profile_path = r'C:\Users\LuanPC\AppData\Local\Google\Chrome\User Data'

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_options.add_argument("profile-directory=Default")  

# Caminho do ChromeDriver
service = Service(r'C:\Users\LuanPC\Documents\pma-script\chromedriver.exe')

# Inicializar o navegador com o serviço
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.instagram.com/')
time.sleep(5)
