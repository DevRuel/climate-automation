from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import datetime
import time

# Configurar opções do Edge 
options = Options()


# Caminho do driver 
service = EdgeService(executable_path="msedgedriver.exe")

# Iniciar navegador
driver = webdriver.Edge(service=service, options=options)

print("Iniciando coleta...")

# Acessar API de clima 
driver.get("https://www.climatempo.com.br/")

# Espera a página carregar 
time.sleep(5)

# Coletar dados
temperatura = driver.find_element(By.CLASS_NAME, "temperature").text
umidade = driver.find_element(By.ID, "current-weather-humidity").text

# Data e hora atual
agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Salvar no arquivo
with open("historico_temperatura.csv", "a", encoding="utf-8") as file:
    file.write(f"{agora},{temperatura},{umidade}\n")

print(f"Coleta realizada em {agora} - Temp: {temperatura} - Umidade: {umidade}")

driver.quit()
