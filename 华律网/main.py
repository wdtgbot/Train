from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as located
from time import sleep as s


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
    driver.get('https://user.66law.cn/consultroom/question.aspx')
    action('//*[@id="u-name"]', 'kingkim')
    action('//*[@id="u-pwd"]', '112233')
    action('//*[@id="form1"]/div[4]/div/div/div/div/p[2]/span/i')
    s(1)
    action('login-btn')
    action('/html/body/div[1]/div/ul/li[1]/div/a[1]')
    for i in range(1, 11):
        question = action(f'//*[@id="list_content"]/div[{str(i)}]/div[1]/span')
        detailed = action(f'//*[@id="list_content"]/div[{str(i)}]/div[2]/div/p[1]')
        print(f"第{i}个问题：{question.get_attribute('innerHTML')}\n{detailed.get_attribute('textContent').replace(' 查看原文>>', '')}")
        s(1)
    driver.close()
    driver.quit()


if __name__ == "__main__":
    try:
        driver = webdriver.Firefox()
    except WebDriverException:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
    main()
