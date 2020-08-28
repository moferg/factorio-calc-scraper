# Factorio Calc Scraper - Marshall Ferguson - 8/2020

# TODO: Figure out template for url to get different results from calc

# base url =    https://kirkmcdonald.github.io/calc.html

# data set =    #data="inset data set"
# data set determines which version of Factorio the recipe is for
# data set should be kept up to date in case of recipe changes

# item =        &items="inset item name"
# item determines which item the recipe is for
# item names will name to exactly match a specific syntax

# factories =   :f:"inset number of factories"
# factories determines the number of factories (assembly machines) working on the recipe
# factories syntax defaults to assembly machine 1, another change to url is needed for assembly machines 2 and 3

# rate =        :r:"inset rate"
# rate determines the rate at which the recipe is worked on
# rate defaults to items/minute, another change to url is needed for items/seond and items/hour

# example url = https://kirkmcdonald.github.io/calc.html#data=1-0-0&items=electronic-circuit:f:1
# example url syntax = base url + data set + items + factories OR rate

# In the future, this script will be able to handle different levels of assembly machines and rates, but for now it will focus on the defaults

# Imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
import time
import math

# print("Welcome to the Facotrio Calc Scraper!")
# time.sleep(1)
# print("This script will scrape the site of the Factorio Calculator to calculate how many assembly machines you need in total for a recipe.")
# time.sleep(2)
# print("All you have to do is answer the following prompts.")
# time.sleep(2)

# item_input = input("What item do you want to make? (If multiple words, must be in following syntax: word1-word2)    ")
# factories_input = input("How many factories will be working on making the item?     ")
# rate_input = input("At what rate do you want to make the item?     ")

# TODO: Request web page

example_url = "https://kirkmcdonald.github.io/calc.html#data=1-0-0&items=electronic-circuit:f:1"
# base_url = "https://kirkmcdonald.github.io/calc.html"
# data_set = "#data=1.0.0"
# # This will be a variable input from the prompt later on, but for now will be hard coded as this version
# item = "&items=" + item_input 
item = "advanced-circuit"
# factories = ":f:" + factories_input
# rate = ":r:" + rate_input                                  

# browser = mechanicalsoup.StatefulBrowser()
# url = base_url + data_set + item + factories
url = example_url
# print(url)
# page = browser.get(url)
# print(page)
# print(page.soup)

# TODO: Automate inputting info into calc site 

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(url)

driver.implicitly_wait(10)

# Not sure why this code doesn't work while the dropdownWrapper selection and clicking does.....

# csv_link = driver.find_element_by_link_text("CSV")
# print(csv_link)
# print(type(csv_link))
# driver.implicitly_wait(5)
# ActionChains(driver).click(csv_link).perform()

item_dropdown = driver.find_elements_by_class_name("dropdownWrapper")[0]
# print(item_dropdown)
# print(type(item_dropdown))
ActionChains(driver).click(item_dropdown).perform()

search_bar = driver.find_element_by_class_name("search")
# print(search_bar)
# print(type(search_bar))
ActionChains(driver).send_keys(item).perform()

item_link = driver.find_element_by_xpath('//img[@alt="' + item + '"]')
# print(item_link)
# print(type(item_link))
ActionChains(driver).click(item_link).perform()

# TODO: Parse through HTML to get total number of assembly machinces needed
    # Figure out how to loop through all the XPaths and put the WebElements in a list
    # Figure out how to extract the text from the html of a list of WebElements

base_elem_path = "/html/body/div[@id='totals_tab']/table[@id='totals']/tr[@class='recipe-row display-row no-mods']"
elem_list = driver.find_elements_by_xpath(base_elem_path)
# print(elem_list)
# print(type(elem_list)) 

assembler_elem_list = []
for i in range(len(elem_list)):
    assembler_elem_list.append(driver.find_element_by_xpath(base_elem_path + "[" + str(i + 1) + "]/td[@class='factory right-align'][1]/tt"))
# print(assembler_elem_list)
# print(type(assembler_elem_list))

assembler_elem_str_list = []
for i in assembler_elem_list:
    assembler_elem_str_list.append(i.get_attribute("innerHTML"))
# print(assembler_elem_str_list)
# print(type(assembler_elem_str_list))

assembler_elem_str_list = ' '.join(assembler_elem_str_list).split()

assembler_elem_float_list = []
for i in assembler_elem_str_list:
    i = i.rstrip("&nbsp;")
    assembler_elem_float_list.append(float(i))
print(assembler_elem_float_list)
print(type(assembler_elem_float_list))

total_num_assemblers = 0
for i in assembler_elem_float_list:
    # print(i)
    i = math.ceil(i)
    # print(i)
    total_num_assemblers += i
print(total_num_assemblers)
print(type(total_num_assemblers))