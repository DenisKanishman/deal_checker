from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to website
driver.get('https://appbrewery.github.io/Zillow-Clone/')

price_elements = driver.find_elements(By.CLASS_NAME, 'PropertyCardWrapper__StyledPriceLine')
address_elements = driver.find_elements(By.TAG_NAME, 'address')
links_elements = driver.find_elements(By.CLASS_NAME, 'StyledPropertyCardDataArea-anchor')

prices = [price_element.text for price_element in price_elements]
addresses = [address_element.text for address_element in address_elements]
links = [links_element.get_attribute('href') for links_element in links_elements]

# Creating a list of dictionaries
data = [{'address': addr, 'price': prc, 'link': lnk} for addr, prc, lnk in zip(addresses, prices, links)]

# link to creating google sheets
driver.get(
    'https://docs.google.com/forms/d/e/1FAIpQLScPoGPotAxH9ZoMy01232yw2-KIptXZI081jiTRdgPdUGXG6w/viewform?usp=sf_link')

address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')
price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')


# filing the data
for i in data:
    address_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd''"]/div[2]/div/div[''2]/div[''1]/div/div/div[''2]/div/div[''1]/div/div[1]/input')))
    price_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[''2]/div/div[2]/div[''2]/div/div/div[''2]/div/div[''1]/div/div[1]/input')))
    link_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="mG61Hd"]/div[''2]/div/div[2]/div[''3]/div/div/div[''2]/div/div[''1]/div/div[1]/input')))
    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')))

    address_input.click()
    address_input.send_keys(i['address'])
    price_input.click()
    price_input.send_keys(i['price'])
    link_input.click()
    link_input.send_keys(i['link'])
    btn.click()
    again = driver.find_element(By.CLASS_NAME, 'c2gzEf').find_element(By.TAG_NAME, 'a')
    again.click()

print('finish')

driver.close()
