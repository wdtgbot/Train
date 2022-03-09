# coding=utf-8
from PIL import Image as image
from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('https://nje.examos.cn/EXAMSF/public/index.jsp')
    driver.save_screenshot(r'./code.png')
    code = driver.find_element_by_id('validateImg')
    left = code.location['x']
    top = code.location['y']
    right = left + code.size['width']
    bottom = top + code.size['height']
    picture = image.open(r'./code.png')
    picture = picture.crop((left, top, right, bottom))
    picture.save(r'./code.png')
    driver.quit()


if __name__ == "__main__":
    main()
