from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import pathlib
import time

def dictionary():
    worlist_path = pathlib.Path(__file__).parent / 'wordlist.txt'
    wordlist = worlist_path.read_text().splitlines()
    return wordlist

def search(driver, word):
    try:
        elem = driver.find_element(By.NAME, "q")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q")))
        elem.clear()
        elem.send_keys(word)
        elem.send_keys(Keys.RETURN)
        if "No results found." in driver.page_source:
            print(f"No se encontraron resultados para '{word}'.")
    except Exception as e:
        print(f"Error al buscar '{word}': {e}")

def search_desktop(driver):
    driver.get("https://www.bing.com/")
    assert "Bing" in driver.title
    time.sleep(5)
    
    wordlist = dictionary()
    for i, word in enumerate(wordlist):
        search(driver,word)
        i+=1

    return print(f"Busquedas Desktop: {i}")


def search_movil(driver):
    driver.get("https://www.bing.com/")
    assert "Bing" in driver.title
    pyautogui.press('f12')
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'm')

    wordlist = dictionary()
    for i, word in enumerate(wordlist):
        search(driver,word)
        i+=1
        if i == 23:
            break

    return print(f"Busquedas Movil: {i}")

if __name__ == '__main__':
    OPTIONS = webdriver.EdgeOptions()
    OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])

    with webdriver.Edge(options=OPTIONS) as driver:
        search_desktop(driver)
        search_movil(driver)
    driver.quit()