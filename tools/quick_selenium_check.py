# tool for checking selemiun functionality on some cases

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.orangehrm.com/'
# header_homepage_xpath = "/html/body/div/div/div/section[1]/div[2]/div/div/div/h1"  # test locator
# header_homepage_xpath = "//div[@class='homepage-slider-content']/h1
a_href_directory_xpath = "//a[@class='oxd-main-menu-item active']"


# get webdriver
ChromeDriverManager(path=r"../../drivers/webdriver_manager_storage").install()
ChromeDriverManager(version='106.0.5249.61').install()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(URL)
print('**** page opened ****')
print(driver.current_url)
print(driver.title)

element = driver.find_element(by=By.XPATH, value=a_href_directory_xpath)

# both methods work as expected - return text content of the tag
print(f"textContent: {element.get_attribute('textContent')}")
print(f"innerText: {element.get_attribute('innerText')}")

element.click()
print(driver.current_url)
print(driver.title)

print('**** page closed ****')

driver.quit()
