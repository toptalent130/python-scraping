def half_scrap(f, driver, index):
    tem = 0
    if index % 2 == 1:
        tem = 50
    # for i in range(0 + tem, 50 + tem):
    for i in range(0 + tem, 2 + tem):
        tds = driver.find_elements_by_xpath("/html/body/form/div[3]/div/div[6]/div[2]/div/table/tbody/tr[" + str(i + 1) + "]/td")
        print("-------------Page:{} Row:{}--------------".format(int(index/2+1),index*50 + i))
        for j in range(2, len(tds)):
            td = driver.find_element_by_xpath("/html/body/form/div[3]/div/div[6]/div[2]/div/table/tbody/tr[" + str(i + 1) + "]/td[" + str(j) + "]")
            print(td.text)
            f.write(td.text + ',')
        f.write('\n')
