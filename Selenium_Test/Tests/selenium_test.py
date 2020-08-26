from selenium import webdriver
import time
import csv
from Pages.catalog_page import CareerCatalogPage

driver = webdriver.Chrome("..\Drivers\chromedriver.exe")
catalog_page = CareerCatalogPage(driver)
catalog_page.load()
time.sleep(4)
career_list = catalog_page.create_list_career()
catalog_page.quit()
with open('..\Files\career_list.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for career in career_list:
        writer.writerow(career)
    file.close()