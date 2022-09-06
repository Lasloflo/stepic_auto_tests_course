from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    x = int(x)
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(link)

    elem = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    print(elem)
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", x_element
    )
    x = x_element.text
    res = calc(x)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(res)

    button_sub = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button_sub.click()

    alert = browser.switch_to.alert
    ans = alert.text
    print(ans)
    alert.accept()

finally:
    browser.quit()