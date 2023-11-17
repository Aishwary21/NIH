import re
import time
from fetching.xpaths import title
from fetching.extraction import address, extract_authors, extract_title
from fetching.save_to_csv import save

def output(driver):
    dict={}
    final_list=list()
    for i in range(1,11): 
        driver.find_element_by_xpath(title(i)).click()
        time.sleep(4)
        
        #title
        title_text=extract_title(driver)
        
        #Authors List
        authors_name=extract_authors(driver)
        
        #Corresponding author
        corressponding_author=authors_name[-1]
        
        #Address
        addr=address(driver)
        full_address=""
        res=[]
        for e in addr:
            res.append(e.replace("\n"," "))
            
        for i in range(0,len(res)):            
            if i==0:
                full_address=full_address+res[i]
            else:
                full_address=full_address+",\n"+res[i]
        
        time.sleep(1)
        
        
        
        #Email
        email=list()
        email_address=""
        if len(addr)!=0:
            for e in addr:
                email=re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", e)
        for e in email:
            email_address=email_address+e
            
            
              
        dict = {
                "Title": title_text,
                "Authors": authors_name,
                "Address": full_address,
                "Email": email_address,
                "Corresponding Author": corressponding_author
            }
        
        
        driver.back()
        
        
        
        final_list.append(dict)
    save(final_list)
    return final_list