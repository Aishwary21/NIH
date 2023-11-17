import time
from fetching.xpaths import search_box, search_button
from fetching.data_as_list import output

def search(driver):
    input="high throughput screening AND INDIA [AD]"
    driver.find_element_by_xpath(search_box()).send_keys(input)
    time.sleep(2)
    driver.find_element_by_xpath(search_button()).click()
    time.sleep(2)
   
    output(driver)
    