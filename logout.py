import time
def logout(driver):
    options_submit = driver.find_element_by_id('cphContent_MessageCenter1_btnLogout').click()
    time.sleep(20)
    return driver
    