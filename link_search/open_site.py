import time
from fetching.search_input import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def open_link():
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://pubmed.ncbi.nlm.nih.gov/")
        
        driver.maximize_window()
        time.sleep(3)
        search(driver)
        time.sleep(3)
        
    except Exception as e:
        print(str(e))
    finally:
        driver.quit()