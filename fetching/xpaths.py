

def search_box():
    return """
        //span/input[@type="search"]
    """
    
def search_button():
    return """
        //div/button[@class="search-btn"]
    """
def title(n):
    return """
        //*[@id="search-results"]//article[{number}]//div/a[1]
    """.format(number=n)
    
def head():
    return """
        //div[@class="full-view"]/h1[@class="heading-title"]
    """

def author(n):
    return """
        //*[@id="full-view-heading"]/div[2]/div/div/span[{number}]/a
    """.format(number=n)
    
def affiliations():
    return """
        //*[@id="full-view-heading"]/div[@class="short-article-details"]
    """

def expand_button():
    return """
        //*[@id="full-view-heading"]/div[@class="short-article-details"]/button
    """
def address_lines(n):
    return """
        //*[@id="full-view-expanded-authors"]/div//li[{number}]
    """.format(number=n)