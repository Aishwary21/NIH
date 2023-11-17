import time
from fetching.xpaths import author, expand_button, head,affiliations,address_lines

def extract_title(driver):
    title=driver.find_element_by_xpath(head()).text
    return title

def extract_authors(driver):
    a =True;
    c=1;
    name=list()
    while(a):
        try:
            n=driver.find_element_by_xpath(author(c)).text
            name.append(n)
            c=(c+1) 
        except Exception as e:
            return name      
            
            
def address(driver):
    addr=list()
    c=1
    try:
        driver.find_element_by_xpath(affiliations()).text
        driver.find_element_by_xpath(expand_button()).click()
        time.sleep(3)
        while (True):
            try:
                ele=driver.find_element_by_xpath(address_lines(c)).text
                c=(c+1)
                addr.append(ele)
            except Exception as e:
                return addr
    except Exception as e:
        return addr
          
    