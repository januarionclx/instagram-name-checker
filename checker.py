# Includes
from selenium import webdriver

# Main
driver = webdriver.Chrome("chromedriver.exe")

# Login
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
driver.find_element_by_name("username").send_keys("USERNAME-HERE")
driver.find_element_by_name("password").send_keys("PASSWORD-HERE")
driver.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(3)

# Checker
with open('usernames') as file:
	for line in file:
		user = line[:-1]

		# Instagram checker
		driver.get('https://instagram.com/{user}'.format(user=user));
		if ("Sorry, this page isn't available." not in driver.page_source):
			print('https://instagram.com/{user}'.format(user=user))

driver.quit()