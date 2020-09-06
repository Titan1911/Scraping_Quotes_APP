
from parsers.quote import QuoteParser
from locators.quote_page_locators import QuotePageLocators

class QuotesPage:
    def __init__(self,browser):
        self.browser = browser
        
    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quote_tags]