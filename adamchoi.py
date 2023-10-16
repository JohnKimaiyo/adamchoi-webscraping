from selenium import webdriver
website="https://www.adamchoi.co.uk/overs/detailed"

driver=webdriver.Chrome()
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matched"]')
all_matches_button.click()




