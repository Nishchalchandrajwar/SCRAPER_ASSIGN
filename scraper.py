from selenium import webdriver
from shutil import which



firefox_path = which("geckodriver")


driver = webdriver.Firefox(executable_path = firefox_path)

driver.implicitly_wait(30) #one can increase the wait to get desired output 

driver.get('https://www.harveynorman.com.au/hp-14-inch-celeron-n4020-4gb-64gb-emmc-laptop.html')

name = driver.find_element_by_xpath('//span[@class="product-name"]')
print(name.text)

driver.find_element_by_xpath('//a[@id ="tab-product-reviews"]').click()
all_items = driver.find_elements_by_xpath('//div[@class ="bv-content-item-author-profile-offset bv-content-item-author-profile-offset-on"]//h3[@class="bv-content-title"]')

total = []

for items in all_items:
    total.append(items.text)

print(total[0])
driver.close()
