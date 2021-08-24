from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

myprofile = webdriver.FirefoxProfile(r'C:\Users\Aloysius\AppData\Roaming\Mozilla\Firefox\Profiles\fcbei8vp.teleScrape')
PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)
df = pd.read_csv('Magpie_Case - Shopee.csv')
final = pd.DataFrame()

driver.get("https://shopee.co.id/")
time.sleep(5)
try :
    close_btn = driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div')
    close_btn.click()
except :
    print("Lanjut scraping")
for ind, row in df.iterrows():
    keyword = row['keyword']
    page = row['number_of_page']
    inputt = driver.find_element_by_xpath('//input[@class="shopee-searchbar-input__input"]')
    inputt.clear()
    inputt.send_keys(keyword)
    search_btn = driver.find_element_by_xpath('//button[@class="btn btn-solid-primary btn--s btn--inline"]')
    search_btn.click()
    time.sleep(5)
    for i in range(1, page+1):
        search_result = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[2]')
        total_result = search_result.find_elements_by_xpath('.//div[@data-sqe="item"]')
        for j in range(len(total_result)):
            item = search_result.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/div['+str(j+1)+']')
            name = item.find_element_by_xpath('.//div[@data-sqe="name"]/div[1]').text
            price = item.find_element_by_xpath('.//span[@class="_24JoLh"]').text
            sold = item.find_element_by_xpath('.//div[@class="go5yPW"]').text
            item_page = driver.find_element_by_xpath('//button[@class="shopee-button-solid shopee-button-solid--primary "]').text
            driver.execute_script("arguments[0].scrollIntoView(true);", item)
            price = price.replace(".","")
            sold = sold.replace(" Terjual","")
            sold = sold.replace(",","")
            sold = sold.replace("RB","000")
            if sold == "":
                sold = 0
            for x in name:
                b = x.isascii()
                if not b:
                    name = name.replace(x, '')
            price = int(price)
            sold = int(sold)
            GMV = price*sold
            data = {
                "Keyword" : keyword,
                "nama_SKU" : name,
                "harga_SKU" : int(price),
                "penjualan" : int(sold),
                "GMV" : int(GMV),
                "Halaman_item" : item_page
            }
            final = final.append(data, ignore_index=True)
        time.sleep(2)
        page_controller = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[3]/div')
        pages = page_controller.find_elements_by_xpath('.//button[@class="shopee-button-no-outline"]')
        button_next_page = driver.find_element_by_xpath('//button[@class="shopee-icon-button shopee-icon-button--right "]')
        next_page_avail = False
        if(i+1<=int(page)):
            for k in pages:
                if int(k.text) == i+1:
                    button_next_page.click()
                    time.sleep(3)
                    next_page_avail = True
                    break
        if(not next_page_avail):
            break
final.to_csv('final.csv')