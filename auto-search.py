from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pathlib
import time


WORDLIST_PATH = pathlib.Path(__file__).parent / 'wordlist.txt'
WORDLIST = WORDLIST_PATH.read_text().splitlines()

OPTIONS = webdriver.EdgeOptions()
OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])

with webdriver.Edge(options=OPTIONS) as driver:
    driver.get("https://www.bing.com/")
    assert "Bing" in driver.title
    time.sleep(7)

    for word in WORDLIST:
        try:
            elem = driver.find_element(By.NAME, "q")
            elem.clear()
            elem.send_keys(word)
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source
        except Exception as e:
            print(f"Error al buscar '{word}': {e}")