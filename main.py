import os
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=14)) + "@gmail.com"
username = "rannDom" + ''.join(random.choices(string.digits, k=4)) # change to your liking
password = "randoM!" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) # change to your liking
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver_path = os.path.join(os.getcwd(), "chromedriver")  # chromedriver in the same directory as the script
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get("https://www.chess.com/register?returnUrl=https://www.chess.com/")


email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "registration_email"))
)
email_field.send_keys(email)
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "registration_username"))
)
username_field.send_keys(username)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "registration_password"))
)
password_field.send_keys(password)
register_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign Up')]"))
)
register_button.click()


WebDriverWait(driver, 10).until(EC.url_matches("https://www.chess.com/home"))

# Save successful credentials to file
folder_path = os.path.join(os.getcwd(), "data")
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
file_path = os.path.join(folder_path, "credentials.txt")
with open(file_path, "a") as f:
    f.write(f"Email: {email}, Username: {username}, Password: {password}\n")

print(f"Registration successful with email: {email}, username: {username} and password: {password}")
driver.quit()
