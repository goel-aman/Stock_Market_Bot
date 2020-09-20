from selenium import webdriver
web = webdriver.Chrome()
web.get('https://www.moneycontrol.com/stocks/histstock.php')
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
time.sleep(4)




from_day = "02"
from_month = "Jan";
from_year = "2020"
to_day = "8"
to_month = "Sep"
to_year = "2020"

company = "Reliance Industries"

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
time.sleep(5)
web.find_element_by_xpath('//*[@id="suggest"]/ul/li[1]/a').click()
time.sleep(3)
Go = web.find_element_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[7]/div[2]/div[6]/table/tbody/tr/td[1]/form/div[4]/input[1]')
Go.click()
time.sleep(5)

window_after = web.window_handles[0]
web.switch_to.window(window_after)

no_of_rows = len(web.find_elements_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[6]/div[4]/table/tbody/tr'))

no_of_cols = len(web.find_elements_by_xpath('//*[@id="mc_mainWrapper"]/div[3]/div[1]/div[6]/div[4]/table/tbody/tr[1]/th'))

print(no_of_rows)
print(no_of_cols)
