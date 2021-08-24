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

df = pd.read_csv("Magpie_Case - Rajasusu.csv")

final = pd.DataFrame()
for ind, row in df.iterrows():
    driver.get(row['url_list'])
    time.sleep(2)
    try :
        button_exit_lokasi = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/button[2]')
        button_exit_lokasi.click()
        time.sleep(1)
    except :
        print("Tidak ada pilih lokasi")
    product_info = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[3]')
    nama_SKU = product_info.find_element_by_xpath('.//h1[@class = "product-title"]').text
    harga = product_info.find_element_by_xpath('.//span[@class = "price-wrapper "]')
    harga_SKU = harga.get_attribute('data-price-amount')
    try :
        stock = product_info.find_element_by_xpath('.//div[@class="out-stock"]').text
    except :
        stock = "Product Available"
    data = {
        "Url" : row['url_list'],
        "nama_SKU" : nama_SKU,
        "harga_SKU" : harga_SKU,
        "stock" : stock
    }
    final = final.append(data, ignore_index=True)

final.to_csv('final.csv')