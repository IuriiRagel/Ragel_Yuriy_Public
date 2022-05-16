import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from configs import CONFIGS
from datetime import datetime


class AmazonTest:

    def __init__(self):

        self.driver = CONFIGS["Driver"]
        self.URL = CONFIGS["URL"]
        self.user = CONFIGS["username"]
        self.password = CONFIGS["password"]
        self.search_key = CONFIGS["search_key"]
        self.Is_loggedin = False
        self.Is_search_result = False
        self.Is_page = False
        self.Cart_empty = True

    def getPage(self):

        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.current_url = self.driver.current_url
        return self.current_url

    def signIn(self):

        self.nav_account_list = self.driver.find_element_by_id("nav-link-accountList").click()
        time.sleep(2)
        self.user_input = self.driver.find_element_by_id("ap_email")
        self.user_input.send_keys(self.user)
        time.sleep(2)
        self.continue_button = self.driver.find_element_by_id("continue")
        time.sleep(1)
        self.continue_button.click()

        self.pass_input = self.driver.find_element_by_id("ap_password")
        self.pass_input.send_keys(self.password)
        time.sleep(2)
        self.submit_button = self.driver.find_element_by_id("signInSubmit")
        time.sleep(1)
        self.submit_button.click()

        self.Is_loggedin = True
        return self.Is_loggedin

    @property
    def signOut(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_id("nav-link-accountList")
        a.move_to_element(m).perform()
        n = self.driver.find_element_by_link_text("Sign Out")
        a.move_to_element(n).click().perform()
        self.Is_loggedin = False
        return self.Is_loggedin


    def top_link(self, i):
        xpath_top_link = '//*[@id="nav-xshop"]/a[' + str(i) + ']'
        self.top_link = self.driver.find_element_by_xpath(xpath_top_link)
        self.top_link.click()
        self.Is_page = True
        return self.Is_page


    def search(self):
        search_box_id = "twotabsearchtextbox"
        self.search_input = self.driver.find_element_by_id(search_box_id)
        self.search_input.click()
        self.search_input.send_keys(self.search_key)
        self.search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        self.search_button.click()
        time.sleep(2)
        self.Is_search_result = True
        return self.Is_search_result

    def open_from_search(self):
        self.item = self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div')
        self.item.click()
        time.sleep(2)
        self.Is_page=True
        return self.Is_page

    def buy_from_pdp(self):
        self.cart_count_before = int(self.driver.find_element_by_xpath('//*[@id="nav-cart-count"]').text)
        self.buy_button = self.driver.find_element_by_id('add-to-cart-button')
        self.buy_button.click()
        time.sleep(2)
        self.cart_count_after = int(self.driver.find_element_by_xpath('//*[@id="nav-cart-count"]').text)
        if self.cart_count_after == self.cart_count_before + 1:
            self.Cart_empty = False

        return self.Cart_empty

    def open_cart(self):
        try:
            self.cart_button = self.driver.find_element_by_partial_link_text('Cart')
        except:
            self.cart_button = self.driver.find_element_by_partial_link_text('cart')
        finally:
            self.cart_button = self.driver.find_element_by_id('nav-cart-count')
        self.cart_button.click()
        time.sleep(2)
        self.Is_page = True
        return self.Is_page

    def delete_from_cart(self):
        self.cart_count = int(self.driver.find_element_by_xpath('//*[@id="nav-cart-count"]').text)
        while self.cart_count > 0:
            self.delete_from_cart_links = self.driver.find_element_by_css_selector('input[value="Delete"][type="submit"][class="a-color-link"]')
            self.delete_from_cart_links.click()
            time.sleep(1)
            self.cart_count = int(self.driver.find_element_by_xpath('//*[@id="nav-cart-count"]').text)
        time.sleep(1)
        if self.cart_count == 0:
            self.Cart_empty == True
        return self.Cart_empty

    def enter_address(self):
        self.enter_address_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "glow-ingress-block")))
        #self.driver.find_element_by_id('glow-ingress-block')
        self.enter_address_link.click()
        self.entry_field = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, "GLUXZipUpdateInput_0")))
        #self.driver.find_element_by_class('class="a-column a-span8"')
        self.entry_field.click()
        self.entry_field.send_keys("M5V4A1")
        self.apply_button = self.driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input')
        self.apply_button.click()
        self.Is_page = True
        return self.Is_page

    def goPage(self):
        self.driver.execute_script("window.scrollTo(0, 1080)")
        self.secondPage = self.driver.find_element_by_class_name('s-pagination-button')
        self.secondPage.click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 1080)")
        time.sleep(1)

        if "page=2" in self.driver.current_url:
            self.Is_page = True
        return self.Is_page

    def addList(self):
        now = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.add_to_WL_button = self.driver.find_element_by_id('add-to-wishlist-button-submit')
        self.WL_dropdown = self.driver.find_element_by_id('wishListDropDown')
        self.WL_dropdown.click()
        self.create_wishlist = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "atwl-dd-create-list")))
        self.create_wishlist.click()
        self.list_name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "list-name")))
        self.list_name_field.click()
        self.list_name_field.send_keys('Testing_shopping_list_', now)
        self.list_create_button = self.driver.find_element_by_xpath('//*[@id="wl-redesigned-create-list"]/span/span/input')
        self.list_create_button.click()
        time.sleep(3)
        self.view_list_button = self.driver.find_element_by_link_text('View Wish List')
        self.view_list_button.click()
        self.driver.save_screenshot('wishlist_confirmation')
        if "wishlist" in self.driver.current_url:
            self.Is_page = True
        return self.Is_page


    def destroyDriver(self):

        self.driver.close()


