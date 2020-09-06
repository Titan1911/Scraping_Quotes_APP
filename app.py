from selenium import webdriver

from pages.quotes_page import QuotesPage


chrome = webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author = input('Enter the name of the author: ')
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
select_tag = input('Enter your tag: ')

page.select_tag(select_tag)
page.search_button.click()

print(page.quotes)
