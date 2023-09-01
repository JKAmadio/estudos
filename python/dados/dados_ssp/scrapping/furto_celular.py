from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def inicializar():
    chromedriver = "./drivers/chromedriver"
    service = ChromeService(executable_path=chromedriver)

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service,  options=chromeOptions)
    driver.set_page_load_timeout(600000)
    driver.get("https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx")
    return driver


def acessar_servico(driver):
    botao_servico = driver.find_element(By.ID, "cphBody_btnFurtoCelular")
    botao_servico.click()


def acessar_ano(driver, numero_ano):
    ano = driver.find_element(By.ID, f"cphBody_lkAno{numero_ano}")
    ano.click()


def acessar_mes(driver, numero_mes):
    mes = driver.find_element(By.ID, f'cphBody_lkMes{numero_mes}')
    wait = WebDriverWait(driver, timeout=2)
    esperando_mes = wait.until(expected_conditions.element_to_be_clickable(mes))
    esperando_mes.click()


def exportar(driver):
    print('dados - inicio')
    exportar = driver.find_element(By.ID, "cphBody_ExportarBOLink")
    wait = WebDriverWait(driver, timeout=2)
    esperando_exportar = wait.until(expected_conditions.element_to_be_clickable(exportar))
    esperando_exportar.click()
    print('dados - fim')


def get_specific_year_complete(ano):
    driver = inicializar()
    acessar_servico(driver)

    print(f'**** ano 20{ano:02d} ****')
    acessar_ano(driver, ano)

    for index in range(12):
        print(f'mes {index + 1:02d}')
        acessar_mes(driver, index + 1)
        exportar(driver)
    time.sleep(10)
    driver.quit()


def get_specific_month(ano, mes):
    driver = inicializar()
    acessar_servico(driver)

    print(f'**** ano 20{ano:02d} ****')
    acessar_ano(driver, ano)

    print(f'mes {mes:02d}')
    acessar_mes(driver, mes)
    exportar(driver)
    time.sleep(10)
    driver.quit()


def get_sequence_of_years(start_year, last_year):
    driver = inicializar()
    acessar_servico(driver)

    for ano in range(start_year, last_year + 1):
        print(f'**** ano 20{ano:02d} ****')
        acessar_ano(driver, ano)

        for index in range(12):
            try:
                print(f'mes {index + 1:02d}')
                acessar_mes(driver, index + 1)
                exportar(driver)
            except TimeoutException:
                print(f'mes {index + 1:02d} - timeout')
                continue
            except ElementClickInterceptedException:
                print(f'mes {index + 1:02d} - elemento nao encontrado')
                continue

        time.sleep(10)
    driver.quit()


def get_list_of_dates(dates):
    driver = inicializar()
    acessar_servico(driver)

    for date in dates:
        print(f'**** ano 20{date[0]:02d} ****')
        acessar_ano(driver, date[0])

        print(f'mes {date[1]:02d}')
        acessar_mes(driver, date[1])
        exportar(driver)
        time.sleep(10)
    driver.quit()
