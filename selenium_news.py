from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Visit website
driver.get("https://news.ycombinator.com")

# Wait for page load
time.sleep(3)

# Find headlines
headlines = driver.find_elements(By.CSS_SELECTOR, ".titleline a")

print("\nTop Headlines Using Selenium:\n")

# Print first 10 headlines
for item in headlines[:10]:
    print(item.text)

# Close browser
driver.quit()