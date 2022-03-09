from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as located


def action(arg1, *arg2):
    locate = located((by.XPATH, arg1)) if "/" in arg1 else located((by.ID, arg1))
    res = wait(driver, 10, 0.5).until(locate)
    driver.execute_script("arguments[0].scrollIntoView();", res)
    res.click()
    if arg2:
        res.send_keys(arg2)
    else:
        return res


def main():
    pass


if __name__ == "__main__":
    try:
        driver = webdriver.Firefox()
    except WebDriverException:
        driver = webdriver.Chrome()
    main()
