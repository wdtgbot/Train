import time

from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as located
from PIL import Image
from requests import post
from os import remove
from hashlib import md5


def chaojiying(username, password, soft_id, codetype):
    driver.save_screenshot(r'./code.png')
    validateImg = driver.find_element_by_id('validateImg')
    left = validateImg.location['x']
    top = validateImg.location['y']
    right = left + validateImg.size['width']
    bottom = top + validateImg.size['height']
    picture = Image.open(r'./code.png')
    picture = picture.crop((left, top, right, bottom))
    picture.save(r'./code.png')
    params = {'user': username, 'pass2': md5(password.encode('utf8')).hexdigest(), 'softid': soft_id, 'codetype': codetype}
    headers = {'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'}
    image = open("./code.png", "rb").read()
    files = {'userfile': ('code.jpg', image)}
    data = post('http://upload.chaojiying.net/Upload/Processing.php',
                data=params, files=files,  headers=headers, proxies={"http": None, "https": None}).json()
    remove("./code.png")
    return data['pic_str']


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
    driver.get("https://nje.examos.cn/EXAMSF/public/index.jsp")
    validate = chaojiying(cjy_username, cjy_password, cjy_softid, cjy_type)
    print(f'验证码：{validate}')
    action("input_userId", fk_username)
    action("input_pwd", fk_password)
    action("input_validate", validate)
    action("login_submit")
    action('//*[@id="inner_menu"]/div/ul/li[7]/a')
    action("option1Idtrue")
    action("option2Idtrue")
    action("submit")
    time.sleep(5)
    driver.close()
    driver.quit()


if __name__ == "__main__":
    cjy_username = ""
    cjy_password = ""
    cjy_softid = ""
    cjy_type = ""  # https://www.chaojiying.com/price.html
    fk_username = ""
    fk_password = ""
    driver = webdriver.Chrome()
    main()
