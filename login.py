import time
def login(driver):
    driver.get('http://www.colerealtyresource.com/login/')
    driver.maximize_window()
    time.sleep(5)
    username = driver.find_element_by_id('txtUserName').send_keys('Homes.n.texas@gmail.com')
    time.sleep(1)
    password = driver.find_element_by_id('txtPassword').send_keys('12345')
    time.sleep(1)
    checkrule = driver.find_element_by_id('chkUserAgreement').click()
    time.sleep(8)
    submit = driver.find_element_by_id('btnLogin').click()
    time.sleep(20)
    return driver
    
    