from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CareerCatalogPage:
  URL = "http://www.espol.edu.ec/es/educacion/grado/catalogo"
  #SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
  def __init__(self, browser):
    self.browser = browser
  def load(self):
    self.browser.get(self.URL)
  def quit(self):
    self.browser.quit()
  def create_list_career(self):
    career_list = []
    elem_list = self.browser.find_elements_by_xpath('//div[@class="panel panel-default"]')
    choices = [elem for elem in elem_list if elem_list.index(elem) % 2 == 0]
    for elem in choices:
      faculty_name = elem.find_element_by_xpath(".//div/h4/a[@role='button']").text.split("\n")[1]
      faculty_career_list = elem.find_element_by_xpath(".//div/div/ul[2]")
      for career in faculty_career_list.find_elements_by_tag_name("li"):
        link_to_career_curriculum = career.find_element_by_xpath(".//a[1]").get_attribute('href')
        career_code = career.find_element_by_tag_name("span").get_attribute("innerHTML")
        career_name_en = career.get_attribute("innerHTML").split(" <a")[0]
        career_list.append((career_name_en,career_code,faculty_name,link_to_career_curriculum))
    return career_list