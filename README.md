# googleFormRentalBot

The goal of this project is to automate filling up google form with data from the rental listings page. 

Code steps:

- getting HTML file of rental listing page using requests.get()

- pulling out data out of HTML file using Beautiful Soup - extracting property address, price per month and web link to property

- using selenium webdriver to automate chrome web browser to interact with google form and automate filling up form data that was extracted by Beautiful Soup - property address, price per month and web link to property

- my google form - https://docs.google.com/forms/d/1Ox4KrwKBs9qzJ5VzPvQOxnbxj81ZrxeI9jnqD4UZo58/prefill
