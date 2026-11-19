from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_locators(browser):
    wait = WebDriverWait(browser, 10)

    browser.get("https://www.saucedemo.com/")

    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.CLASS_NAME, "submit-button")
    browser.find_element(By.TAG_NAME, "form")
    browser.find_element(By.XPATH, "//input[@name='user-name' and @type='text']")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    browser.find_element(By.CSS_SELECTOR, "[data-test='social-x']")
    browser.find_element(By.CSS_SELECTOR, "[data-test='social-facebook']")

    browser.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    browser.find_element(By.XPATH, "//button[text()='Add to cart']")
    browser.find_element(By.XPATH, "//img[contains(@alt, 'Bike Light')]")
    browser.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")

    browser.find_element(By.XPATH, "//select[contains(@class, 'product_sort_container')]/ancestor::div[1]")
    browser.find_element(By.XPATH, "//div[@id='inventory_container']/descendant::img[1]")
    browser.find_element(By.XPATH, "//select[contains(@class, 'product_sort_container')]/following::div[1]")
    browser.find_element(By.XPATH, "//select[@class='product_sort_container']/parent::*[1]")
    browser.find_element(By.XPATH, "//select[contains(@class, 'product_sort_container')]/preceding::*[1]")

    browser.find_element(By.CSS_SELECTOR, ".product_sort_container")
    browser.find_element(By.CSS_SELECTOR, ".btn.btn_primary")
    browser.find_element(By.CSS_SELECTOR, ".product_sort_container option")
    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)")
    browser.find_element(By.CSS_SELECTOR, "select")
    browser.find_element(By.CSS_SELECTOR, "select.product_sort_container")
    browser.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']")
    browser.find_element(By.CSS_SELECTOR, "[class~='product_sort_container']")
    browser.find_element(By.CSS_SELECTOR, "[data-test|='add-to-cart']")
    browser.find_element(By.CSS_SELECTOR, "[class^='product']")
    browser.find_element(By.CSS_SELECTOR, "[class$='container']")
    browser.find_element(By.CSS_SELECTOR, "[class*='sort']")

    browser.get("https://www.saucedemo.com/cart.html")
    browser.find_element(By.XPATH, "//button[@data-test='checkout']")