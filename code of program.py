from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.prestizolinija.lt/admin')
username = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr/td/center/form/table[2]/tbody/tr[1]/td[2]/input').send_keys('admin')
time.sleep(1)
password = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr/td/center/form/table[2]/tbody/tr[2]/td[2]/input').send_keys('labas55')
time.sleep(1)
submit = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr/td/center/form/table[2]/tbody/tr[3]/td[2]/input').click()
time.sleep(4)
kalo = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[1]/td/div/ul/li[2]/a').click()
time.sleep(4)
total_links = []
total_sku = []
total_products = driver.find_elements_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/a')
links = driver.find_elements_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/div/table/tbody/tr/td[10]/a')
for t in total_products:
    total_sku.append(t.text)
    total_links.append(t.get_attribute('href'))

for l in range(1,len(total_links)):
    driver.get(total_links[l])
    sku = total_sku[l]
    name = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/div/form/fieldset/table/tbody/tr[3]/td[2]/input').get_attribute('value').replace(',','')
    price = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/div/form/fieldset/table/tbody/tr[7]/td[2]/input').get_attribute('value').replace(',','')
    id = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/div/form/fieldset/table/tbody/tr[4]/td[2]/input').get_attribute('value').replace(',','')
    category = driver.find_elements_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/div/form/fieldset/table/tbody/tr[1]/td[2]/select/option')
    cath = ''
    for c in category:
        if c.get_attribute('selected'):
            cath = c.text.replace(',','')
    driver.switch_to.frame('description_ifr')
    descrip = driver.find_element_by_xpath('//*[@id="tinymce"]').text.replace(',','').replace("\n",".")
    driver.switch_to.default_content()
    pic_url = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/div/form/fieldset/table/tbody/tr[14]/td[2]/a[1]/img').get_attribute('src')
    with open('samplefroclient.csv','a', encoding='utf-8') as f:
        f.write(sku + ',' + name + ',' + price + ',' + id + ','  + descrip +',' + cath + ',' + pic_url + '\n')