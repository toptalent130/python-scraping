import time
import pickle
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from login import *
from logout import *
from readZipCode import *
from half_scrap import *
all_zip_codes = readZipCode()
driver = webdriver.Chrome(ChromeDriverManager().install())
cookie_accept = True
with open('result.csv','a', encoding='utf-8') as f:
    for each_zip in all_zip_codes:
        for iterater in range(0,200):
            page_index = int(iterater/2+1)
            driver = login(driver)
            if cookie_accept:
                checkcookie = driver.find_element_by_id('hs-eu-confirmation-button').click()
                time.sleep(8)
                cookie_accept = False
            if page_index == 1:
                prospect_IQ = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[7]/div[1]/div/div/ul/li[2]/a').click()
                time.sleep(5)
            zipcode = driver.find_element_by_id('cphContent_cphMainContent_Search1_PremiumDataSearch_txtZipCodes').send_keys(str(each_zip))
            time.sleep(5)
            searchclick = driver.find_element_by_id('cphContent_cphMainContent_Search1_PremiumDataSearch_btnSearch').click()
            time.sleep(20)
            click1500 = driver.find_element_by_id('confirm-dialog-ok').click()
            time.sleep(5)
            # double click operation and perform
            advanced_options_link = driver.find_element_by_id('advanced-options-link')
            action = ActionChains(driver)
            action.double_click(advanced_options_link).perform()
            time.sleep(5)
            if page_index%2 == 0:
                options = driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/table/tbody/tr/td/a[3]").click()
                time.sleep(5)
            options_submit = driver.find_element_by_id('cphContent_cphMainContent_SearchResults_btnSubmitAdvancedOptions').click()
            time.sleep(15)
            if page_index > 11:
                if page_index == 11:
                    page11_click = driver.find_element_by_xpath("/html/body/form/div[3]/div/div[6]/div[2]/div/table/tfoot/tr/td/table/tbody/tr/td[2]/div[2]/a[11]").click()
                    time.sleep(15)
                else:
                    pagemore11_click = driver.find_element_by_xpath("/html/body/form/div[3]/div/div[6]/div[2]/div/table/tfoot/tr/td/table/tbody/tr/td[2]/div[2]/a[12]").click()
                    time.sleep(15)
            if page_index > 1:
                checkcookie = driver.find_element_by_class_name('rgPageNext').click()
                time.sleep(15)
            half_scrap(f, driver, iterater)
            driver = logout(driver)
# login(driver)
# logout(driver)
# driver.execute_script("""
#             var theForm = document.forms['aspnetForm'];
#             theForm.__EVENTTARGET.value = 'ctl00$ctl00$cphContent$cphMainContent$SearchResults$rgSearchResults$ctl00$ctl03$ctl01$ctl23';
#             theForm.__EVENTARGUMENT.value = '';
#             theForm.submit();
#         """)

# pre_iterater = 0
# while pre_iterater < 85:
#     checkcookie = driver.find_element_by_class_name('rgPageNext').click()
#     time.sleep(10)
#     pre_iterater = pre_iterater + 1

# with open('result2.csv','a', encoding='utf-8') as f:
#     iterater = 0
#     while iterater < 100:
#         table_tbody_rws = driver.find_elements_by_xpath("/html/body/form/div[3]/div/div[6]/div[2]/div/table/tbody/tr")
#         time.sleep(8)
#         for i in range(0,len(table_tbody_rws)):
#             tds = driver.find_elements_by_xpath("/html/body/form/div[3]/div/div[6]/div[2]/div/table/tbody/tr[" + str(i + 1) + "]/td")
#             print("-------------Row Number: {}--------------".format(iterater*100 + i))
#             for j in range(2, len(tds)):
#                 td = driver.find_element_by_xpath("/html/body/form/div[3]/div/div[6]/div[2]/div/table/tbody/tr[" + str(i + 1) + "]/td[" + str(j) + "]")
#                 print(td.text)
#                 f.write(td.text + ',')
#             f.write('\n')
#         checkcookie = driver.find_element_by_class_name('rgPageNext').click()
#         time.sleep(7)
#         iterater = iterater + 1

# -----Jquery Import------------
# driver.execute_script("""
# var script = document.createElement( 'script' );
# script.type = 'text/javascript';
# script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js';
# document.head.appendChild(script);
# """)
# ------------------------------

# -------Export driver to html-------
# pageSource = driver.page_source
# fileToWrite = open("page_source.html", "w")
# fileToWrite.write(pageSource)
# -----------------------------------

#--------Read and Write Cookie----------------
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# checkcookie = driver.find_element_by_id('hs-eu-confirmation-button').click()
# time.sleep(8)
# -------------------------------------
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.get('http://www.colerealtyresource.com/search/')
# ---------------------------------------
