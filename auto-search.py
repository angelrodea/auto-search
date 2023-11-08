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

OPTIONS = webdriver.EdgeOptions()
OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])

with webdriver.Edge(options=OPTIONS) as driver:
    driver.get("https://www.bing.com/")
    assert "Bing" in driver.title
    time.sleep(5)
    for i, word in enumerate(WORDLIST):
        try:
            elem = driver.find_element(By.NAME, "q")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q")))
            elem.clear()
            elem.send_keys(word)
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source
            i+=1
        except Exception as e:
            print(f"Error al buscar '{word}': {e}")

print(f"Total de busquedas: {i}")


with webdriver.Edge(options=OPTIONS) as driver:
    driver.get("https://www.bing.com/")
    assert "Bing" in driver.title
    time.sleep(5)
    pyautogui.press('f12')
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'm')

    for i, word in enumerate(WORDLIST):
        try:
            elem = driver.find_element(By.NAME, "q")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q")))
            elem.clear()
            elem.send_keys(word)
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source
            if i == 23:
                break
        except Exception as e:
            print(f"Error al buscar '{word}': {e}")

print(f"Total de busquedas (movil): {i}")
driver.quit()