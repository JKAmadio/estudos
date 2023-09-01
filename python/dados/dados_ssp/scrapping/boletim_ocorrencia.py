from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service as ChromeService
import time


def init_driver():
    chromedriver = "./drivers/chromedriver"
    service = ChromeService(executable_path=chromedriver)

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service,  options=chromeOptions)
    driver.get("https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx")
    return driver


def acessar_servico(driver, service_name):
    botao_servico = driver.find_element(By.ID, f"cphBody_btn{service_name}")
    botao_servico.click()


def acessar_ano(driver, numero_ano):
    ano = driver.find_element(By.ID, f"cphBody_lkAno{numero_ano}")
    ano.click()


def acessar_mes(driver, wait, numero_mes):
    mes = driver.find_element(By.ID, f'cphBody_lkMes{numero_mes}')
    time.sleep(5)
    esperando_mes = wait.until(expected_conditions.element_to_be_clickable(mes))
    esperando_mes.click()


def exportar(driver, wait):
    print('dados - inicio')

    exportar = driver.find_element(By.ID, "cphBody_ExportarBOLink")

    esperando_exportar = wait.until(expected_conditions.element_to_be_clickable(exportar))
    esperando_exportar.click()
    print('dados - fim')




driver = init_driver()
acessar_servico(driver, "FurtoCelular")
