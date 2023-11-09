from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import pathlib
import time

WORDLIST_PATH = pathlib.Path(__file__).parent / 'wordlist.txt'
WORDLIST = WORDLIST_PATH.read_text().splitlines()

def search(driver):
    for i, word in enumerate(WORDLIST):
        try:
            elem = driver.find_element(By.NAME, "q")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q")))
            elem.clear()
            elem.send_keys(word)
            elem.send_keys(Keys.RETURN)
            if "No results found." in driver.page_source:
                print(f"No se encontraron resultados para '{word}'.")
            i+=1
        except Exception as e:
            print(f"Error al buscar '{word}': {e}")
    return i

def search_desktop(driver):
    driver.get("https://www.bing.com/")
    assert "Bing" in driver.title
    time.sleep(5)
    num_search = search(driver)

    return print(f"Busquedas Desktop: {num_search}")


def search_movil(driver):
    driver.get("https://www.bing.com/")
    assert "Bing" in driver.title
    pyautogui.press('f12')
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'm')

    num_search = search(driver)

    return print(f"Busquedas Movil: {num_search}")


def main():
    OPTIONS = webdriver.EdgeOptions()
    OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])

    with webdriver.Edge(options=OPTIONS) as driver:
        search_desktop(driver)
        search_movil(driver)
    driver.quit()

if __name__ == '__main__':
    main()