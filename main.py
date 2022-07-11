'''
install pyinstaller...
--> used to convert .py to executable file(.exe)
--> commands:  pyinstaller --onefile filename // in my case it's main.py and make sure you are in the directory
                                                 where your python file is.
-->Then 2 folder will be created build and dist. The executable file is in dist folder
--> Run the .exe file  (openwith terminal)

To schedule the executable
--> can use crontab === crontab.guru to create command
--> command: time file_path
'''
#we want driver--> allows to interact with website through selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.chrome.options import Options ##importing this library so that the program doesn't open the webpage
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
# MMDDYYYY
month_day_year = now.strftime("%m%d%Y")  # string from time.  for syntax visit strftime.org


website = "https://www.thesun.co.uk/sprts/football/"
path = r"C:/Users/DELL/OneDrive/Desktop/python/chromedriver_win32/chromedriver.exe"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options) # options variable used for headless mode
driver.get(website) #if you run till here opens the website

b=driver.find_element(by="xpath", value='//div[@class="teaser__copy-container"]') #find_element gives only first element

''' b=driver.find_element(by="xpath", value='//div[@class="teaser__image-container"]/a/img') #find_element gives only first element
print(b.get_attribute('src'))'''

container = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]') #returns list

titles = []
subtitles = []
links = []

for c in container:
    title = c.find_element(by="xpath", value='./a/h2').text
    subtitle = c.find_element(by="xpath", value='./a/p').text
    link = c.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'titles': titles, 'subtitles': subtitles, 'links': links}

df_headlines = pd.DataFrame(my_dict)

# using forward-slash(/) may cause trouble due to diff OS so we use os module
file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()
#//div[@class="teaser__copy-container"]


