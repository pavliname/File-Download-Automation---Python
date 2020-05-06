import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
# For using sleep function because selenium
# works only when the all the elements of the
# page is loaded.
import time
#import sys

from selenium.webdriver.chrome.options import Options

load_dotenv()

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\pmendlova\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

# webdriver path set
browser = webdriver.Chrome("C:\Users\pmendlova\Downloads\chromedriver.exe")
#browser = webdriver.Ie("C:\Users\pmendlova\Downloads\IEDriverServer.exe")
# To maximize the browser window
browser.maximize_window()

# link set
browser.get(os.getenv("URL"))

time.sleep(3)
# Enter your user name and password here.
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# username send
a = browser.find_element_by_name('username')
a.send_keys(username)

# password send
b = browser.find_element_by_name('j_password')
b.send_keys(password)

# submit button clicked
browser.find_element_by_xpath("//*[@value = 'Invio']").click()

time.sleep(15)

# submit button clicked
browser.find_element_by_class_name('MenuSupAttivo').click()

time.sleep(15)

# submit button clicked to go to Data
browser.find_element_by_id('webfx-tree-object-3-anchor').click()

time.sleep(15)

page_source = browser.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# download new files

table = soup.find_all('table',{'width':'100%'},{'class':'Lista'})[7]
id_no = 0
id = {}
for row in table.find_all('tr'):
		if 'In linea' in row.text:
			id_no +=1
			cell = row.find_all('td')[0].text[21:32]
			cells = cell.strip()
			browser.find_element_by_xpath("//input[@name='RESID'][@type='checkbox'][@value='"+ cells +"']").click()
			time.sleep(15)
			browser.find_element_by_link_text('SCARICA SELEZIONATI').click()
			time.sleep(30)
			id[id_no] = [cell]


print('Login Successful')
print('IDs of the files downloaded:')
print(id)
browser.close()
