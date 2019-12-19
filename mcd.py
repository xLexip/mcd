import time
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

def form(cdeP):
    timex = 0.4
    browser = webdriver.Chrome('/home/robin/Documents/mcd/chromedriver')
    browser.get('https://mcdonalds.fast-insight.com/voc/de/de')
    time.sleep(4)
    codeInput = browser.find_element_by_id('receiptCode')
    codeInput.send_keys(cdeP)
    browser.find_element_by_xpath('//button[text()="LOS"]').click()
    time.sleep(1)
    while browser.current_url=="https://mcdonalds.fast-insight.com/voc/de/de":
        browser.refresh()
        cdeP = cde(cdeP)
        time.sleep(0.6)
        codeInput = browser.find_element_by_id('receiptCode')
        codeInput.send_keys(cdeP)
        browser.find_element_by_xpath('//button[text()="LOS"]').click()
        time.sleep(0.7)
    time.sleep(5)
    #----------------------------------------------------------------------------------------------------
    btnNext = browser.find_element_by_id('next-sbj-btn')
    def nxt():
        btnNext.click()
        time.sleep(timex)
    

    for x in range(0,5):
        browser.find_element_by_xpath(".//div[normalize-space(@class)='rating'][@rel='4']").click()
        btnNext.click()   
        time.sleep(timex) 

    browser.find_element_by_class_name('option').click()
    nxt() 
    browser.find_element_by_class_name('option').click()
    nxt() 
    browser.find_element_by_class_name('politeText').send_keys('-')
    nxt() 
    browser.find_element_by_class_name('option').click()
    nxt() 
    browser.find_element_by_class_name('option').click()
    nxt()
    browser.find_element_by_xpath("//select[@name='sbj_1005528[]']/option[text()='1']").click()
    nxt()
    browser.find_element_by_xpath("//select/option[text()='0']").click()
    nxt()
    browser.find_element_by_class_name('option').click()
    nxt()
    browser.find_element_by_class_name('option').click()
    nxt()
    browser.find_element_by_class_name('option').click()
    nxt()
    browser.find_element_by_class_name('btn').click()
    time.sleep(4)
    #----------------------------------------------------------------------------------------------------
    browser.save_screenshot("/home/robin/mcdcodes/"+cdeP + ".png")
    form(cde(cdeP))

def cde(str):
    str = cdeRZ(str)
    tmp = str[-1:]
    tmp = chr(ord(tmp)+1)
    str = str[:-1]
    str = str + tmp
    return str
        
def cdeRZ(str):
    tmp = str[-1:]
    if tmp=="z":
        tmp1 = str[-2:]
        tmp1 = tmp1[:-1]
        tmp1 = chr(ord(tmp1)+1)
        str = str[:-2]
        str = cdeRZ(str + tmp1) + "a"
    return str


form(input(": "))