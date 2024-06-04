#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller

import pyzipper
import shutil
import time
import os
import sys

def unzip_file(file_path):
    with pyzipper.AESZipFile(file_path) as zf:
        zf.extractall(path='./data')

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def days_in_month(month, leap_year):
    if month == 1:  # January
        return 31
    elif month == 2:  # February
        return 29 if leap_year else 28
    elif month == 3:  # March
        return 31
    elif month == 4:  # April
        return 30
    elif month == 5:  # May
        return 31
    elif month == 6:  # June
        return 30
    elif month == 7:  # July
        return 31
    elif month == 8:  # August
        return 31
    elif month == 9:  # September
        return 30
    elif month == 10:  # October
        return 31
    elif month == 11:  # November
        return 30
    elif month == 12:  # December
        return 31

def iterate_year(year):
    leap_year = is_leap_year(year)
    first_loop = True
    for month in range(1, 13):
        for day in range(1, days_in_month(month, leap_year) + 1):
            target = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/main/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]'))
            )
            action = ActionChains(driver)
            action.move_to_element(target).perform()
            menu_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/main/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[4]/button[2]/div'))
            )
            menu_item.click()
            time.sleep(1)
            if first_loop:
                granularity = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[1]'))
                )
                granularity.click()
                button_1m = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/ul/li[2]'))
                )
                button_1m.click()
            start_date = f'{year}-{month:02d}-{day:02d}'
            input_start_date = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/label/div[2]/div/div[1]/input'))
            )
            input_start_date.click()
            input_start_date.send_keys(start_date)
            end_date = f'{year}-{month:02d}-{day:02d}'
            input_end_date = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/label/div[2]/div/div[3]/input'))
            )
            input_end_date.click()
            input_end_date.send_keys(end_date + Keys.RETURN)
            if first_loop:
                symbol = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[1]'))
                )
                symbol.click()
                input_box = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div/input'))
                )
                input_box.send_keys(name)
                select_box = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[3]/ul/div/div/li[1]'))
                )
                select_box.click()
            button_confirm = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/div[2]/form/div/div[2]/div/button'))
            )
            button_confirm.click()
            button_download = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/div/div/form/div[2]/div[2]/button[2]'))
            )
            button_download.click()
            time.sleep(2)
            shutil.move(f'/path/to/Downloads/{name}-1m-{start_date}.zip', f'/path/to/Binance_Backtester/data')
            unzip_file(f'/path/to/Binance_Backtester/data/{name}-1m-{start_date}.zip')
            os.remove(f'/path/to/Binance_Backtester/data/{name}-1m-{start_date}.zip')
            if first_loop:
                first_loop = False

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.binance.com/en/landing/data" )
time.sleep(3)

name = "BTCUSDT"
backtesting_folder = './data'
     
if not os.path.isdir(backtesting_folder):
    os.mkdir(backtesting_folder)

while True:
    iterate_year(2022)
    
print("exit")
sys.exit()
