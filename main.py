from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

## URL for rental listings in San Francisco - up to $3000 per month, 1+bedroom
listings_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
# URL for google form where the data will be automatically added - address of the property, price per month and web link to property
form_url = "my_google_form"

# headers for get request to access listings url - headers can be checked on http://myhttpheader.com/
headers = {
    "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
}

# accessing listings page and getting html file for that page
response = requests.get(url=listings_url, headers=headers)
response.raise_for_status()
html_file = response.text

soup = BeautifulSoup(html_file, "html.parser")
links_data = []
# getting all listing properties on the page with their respective div
all_data = soup.find_all(name="div", class_="list-card-info")
# extracting property links from html file
for link in all_data:
    link_add = str(link).split("href=\"")[1].split("\" tabindex")[0]
    # some links are missing "https://www.zollow.com" part so it has to be added
    if "https" not in link_add:
        link_add = "https://www.zollow.com" + link_add
    print(link_add)
    links_data.append(link_add)
# extracting property addresses from html file
address_data = soup.find_all(name="address", class_="list-card-addr")
# extracting property prices from html file
prices_data = soup.find_all(name="div", class_="list-card-price")

chrome_driver_path = "<path to my chrome driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for i in range(len(links_data)):
    # accessing the google form
    driver.get(form_url)
    # finding the address input field
    address_input = driver.find_element_by_css_selector('[aria-labelledby="i1"]')
    address_input.click()
    time.sleep(1)
    # entering the address to address input
    address_input.send_keys(address_data[i].text)
    # finding the price input field
    price_input = driver.find_element_by_css_selector('[aria-labelledby="i5"]')
    price_input.click()
    time.sleep(1)
    # entering the price to price input
    price_input.send_keys(prices_data[i].text)
    # finding the link input field
    link_input = driver.find_element_by_css_selector('[aria-labelledby="i9"]')
    link_input.click()
    time.sleep(1)
    # entering the link to link input
    link_input.send_keys(links_data[i])
    # sending completed form for each listing property
    send_btn = driver.find_element_by_css_selector('[role="button"]')
    send_btn.click()
    time.sleep(2)
driver.quit()








