from selenium import webdriver
import pandas as pd
from pandas import DataFrame
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta

def Stock_Dataset(from_day,from_month,from_year,to_day,to_month,to_year,company):
    web = webdriver.Chrome()
    web.get('https://www.moneycontrol.com/stocks/histstock.php')
    time.sleep(6)
    FromDate = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[2]/select[1]')
    FromDate.send_keys(from_day)

    FromMonth = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[2]/select[2]')
    FromMonth.send_keys(from_month)

    FromYear = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[2]/select[3]')
    FromYear.send_keys(from_year)


    toDate = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[4]/select[1]')
    toDate.send_keys(to_day)

    toMonth = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[4]/select[2]')
    toMonth.send_keys(to_month)

    toYear = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[4]/select[3]')
    toYear.send_keys(to_year)

    Company = web.find_element_by_xpath('//*[@id="mycomp"]')
    Company.send_keys(company)
    time.sleep(10)
    Company.send_keys(" ");
    time.sleep(2)
    web.find_element_by_xpath('//*[@id="suggest"]/ul/li[1]/a').click()
    time.sleep(6) 
    Go = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[4]/input[1]')
    Go.click()
    time.sleep(6)

    window_after = web.window_handles[0]
    web.switch_to.window(window_after)

    no_of_rows = len(web.find_elements_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[6]/div[4]/table/tbody/tr'))
    no_of_cols = len(web.find_elements_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[6]/div[4]/table/tbody/tr[1]/th'))

    dataset = []

    for row in range(3,no_of_rows + 1):
        datasetrow = []
        for column in range(1,no_of_cols + 2):
            value = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[6]/div[4]/table/tbody/tr[' + str(row) + ']/td[' + str(column) + ']').text
            datasetrow.append(value)
        dataset.append(datasetrow)

    dict_dataset = {'Date': [], 'Open' : [], 'High' : [], 'Low': [], 'Close': [], 'Volume': [],'High-Low': [], 'Open-Close': []}

    column_name = ['Date', 'Open','High','Low','Close','Volume','High-Low','Open-Close']

    for i in range(0,len(dataset)):
        for j in range(0,no_of_cols  +1):
            dict_dataset[column_name[j]].append(dataset[i][j])

    df = pd.DataFrame(dict_dataset)
    df['Open'] = df['Open'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['Close'] = df['Close'].astype(float)
    df['Volume'] = df['Volume'].astype(float)
    df['High-Low'] = df['High-Low'].astype(float)
    df['Open-Close'] = df['Open-Close'].astype(float)
    # df['Date'] = pd.to_datetime(df['Date'])

    return df

"""
dummy data to dry run the code.
"""

today = date.today()
current_date = today.strftime("%b%d%Y")  
month_old_date = (date.today()-timedelta(days=150)).strftime("%b%d%Y")
print(month_old_date)
###############################################################################
from_day = month_old_date[3:5]
from_month = month_old_date[0:3]
from_year = month_old_date[5:]
to_day = current_date[3:5]
to_month = current_date[0:3]
to_year = current_date[5:]
company = "Hero Motocorp"
# ################################ End Of Dummy Data #############################
m = Stock_Dataset(from_day,from_month,from_year,to_day,to_month,to_year,company)
m.to_csv(company + '.csv')
print(m)