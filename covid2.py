from bs4 import BeautifulSoup, element
import os
import sys
import time
from threading import Thread
import re
import requests
from sys import platform
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# python -m pip install win10toast
from win10toast import ToastNotifier
# To check if any notifications are active,
# use `toaster.notification_active()`
# One-time initialization
toaster = ToastNotifier()


def init_chrome_driver():
    directory = os.path.abspath(os.path.dirname(__file__))
    if os.name == 'nt':
        chrome_driver = '\chromedriver.exe'
    else:
        sys.exit('Program works on windows only.')
    driver_exe = 'chromedriver'
    options = Options()
    options.add_argument("--headless")
    # driver = webdriver.Chrome(directory + chrome_driver)
    driver = webdriver.Chrome(driver_exe, options=options)
    
    driver.maximize_window()
    return driver

class AutoCheck:
    def __init__(self, url, state):
        
        self.url = url
        self.state = state
        self.driver = init_chrome_driver()
        
        try:
            self.driver.get(self.url)
        except:
            self.driver.quit()
            sys.exit('Invalid URL address.')
    
    def quit_driver(self):
        self.driver.quit()

    def take_screenshot(self):
        self.driver.save_screenshot('screenshot.png')
    
    def check(self):
        time.sleep(20)
        link_rows = self.driver.find_elements_by_class_name('link__row')
        for link_row in link_rows:
            if link_row.find('span').text == self.state:
                link_row.find('a').click()
        time.sleep(10)
        available_cities = []
        modal_table = self.driver.find_element_by_class_name('modal--active')
        cities = modal_table.find_element_by_tag_name('tbody').find(tr)
        for city in cities:
            if city.find('span')[1].text == 'Available':
                available_cities.append(city.find('span')[0].text)
        if len(available_cities) > 0:
            alert_str = "Available Cities in " + self.state + "\n"
            for city in available_cities:
                alert_str = alert_str + city + "\n"
            # Show notification 
            toaster.show_toast("Notification!", alert_str, threaded=True,
                   icon_path=None, duration=30)  # 30 seconds
            while toaster.notification_active():
                time.sleep(0.1)
        self.driver.close()


if __name__ == '__main__':
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }
    
    url = 'https://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-link2-coronavirus-vaccine'
    # bot = AutoCheck(url, state)
    while True:
        print('Please Input the name of state: ')
        state = str(raw_input())
        if state in us_state_abbrev.keys():
            print("Got it.")
            try:
                bot = AutoCheck(url, state)
                while True:
                    time.sleep(300)
                    bot.check()
                sys.exit(0)
            except KeyboardInterrupt:
                sys.exit(1) 
        else:
            print("Your input is incorrect.")
            continue