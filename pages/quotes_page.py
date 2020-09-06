from selenium.webdriver.support.ui import Select

from parsers.quote import QuoteParser
from locators.quote_page_locators import QuotePageLocators


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser
        
    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quote_tags]
    
    @property
    def author_dropdown(self):
        element = self.browser.find_element_by_css_selector(QuotePageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    @property
    def tag_dropdown(self):
        element = self.browser.find_element_by_css_selector(QuotePageLocators.TAG_DROPDOWN)
        return Select(element)

    def get_available_tags(self):
        return [option.text.strip() for option in self.tag_dropdown.options]

    def select_tag(self, tag_name):
        self.tag_dropdown.select_by_visible_text(tag_name)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(QuotePageLocators.SEARCH_BUTTON)