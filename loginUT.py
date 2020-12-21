from PIL import Image, ImageEnhance, ImageFilter
from selenium import webdriver
from requests import get
from selenium.webdriver.chrome.options import Options
import pytesseract
import requests
import shutil
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.file_detector import UselessFileDetector
import pyautogui
import autoit


import sys
from random import randint
from time import sleep


UT_URL = "https://sv.ut.edu.vn/Default.aspx"

def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))

def islogin(driver):
    # print('islogin')
    try:
        driver.find_element_by_css_selector("#ctl00_ucRight1_btnLogin")
        return 0
    except:
        return 1
    
    
def nhapdata(driver):
    # print('nhapdata')
    # driver.get(UT_URL)
    cc = driver.find_element_by_css_selector("#imgSecurityCode")
    macapcha = cc.get_attribute("src")
    response = requests.get(macapcha, stream=True)
    with open('capcha.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    img = Image.open("capcha.png")
    img = img.convert('RGB')
    pix = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)
    img.save('capcha.png')
    text = pytesseract.image_to_string(Image.open('capcha.png'))
    # print(text)
    msv = driver.find_element_by_css_selector('#ctl00_ucRight1_txtMaSV')
    msv.clear()
    msv.send_keys("1851120028")  
    pwd = driver.find_element_by_css_selector('#ctl00_ucRight1_txtMatKhau')
    pwd.clear()
    pwd.send_keys("namzlinhjnk0ut")  
    capcha = driver.find_element_by_css_selector('#ctl00_ucRight1_txtSercurityCode')
    capcha.clear()
    capcha.send_keys(text)
    # random_sleep(2000,3000)
    # print("try")

    try:
        # print("alert")
        driver.switch_to().alert().dismiss()
        # print("hmm")
        nhapdata(driver)
    except:
        return 1
    return 1
    # driver.find_element_by_css_selector('#ctl00_ucRight1_btnLogin').click()
    

def chuplichhoc(driver):
    # print('chuplichhoc')
    
    driver.get("https://sv.ut.edu.vn/LichHocLichThiTuan.aspx")
    # sleep(randint(1000, 2000))
    #chup man hinh
    try:
        lich = driver.find_element_by_css_selector("#main_container > div.col-full.clearfix > div.col-left > div.main-content > div.div-ChiTietLich")
        lich.screenshot("lich.png")
    except :
        Login(driver)
    
    

def Login(driver):
    nhapdata(driver)
    if islogin(driver) == 0:
        Login(driver)
    chuplichhoc(driver)
    
    return 0

def loginmain():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(UT_URL)
    Login(driver)
    driver.close()
    return 0

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path=r'C:\Users\efert\.wdm\drivers\chromedriver\win32\87.0.4280.88\chromedriver.exe')

# if __name__ == '__main__':
#     loginmain()