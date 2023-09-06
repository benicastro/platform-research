# Import needed modules/libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create driver with Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
driver.get("https://gab.com/worth__fighting__for/")

##############################################
# Extract the information needed #############
##############################################

# Create a dictionary to contain all information
info = {}

info["user_name"] = driver.find_element(
    By.CLASS_NAME,
    value="_3_54N _1-fAn _317eq mVHNg _2ZzNB _3XmA1 _1kAFo Y32gl".replace(" ", "."),
).text

info["date_joined"] = driver.find_element(
    By.CLASS_NAME,
    value="_33mR1 _UuSG _3_54N a8-QN _2cSLK L4pn5 RiX17".replace(" ", "."),
).text[13:]

info["user_image"] = driver.find_element(
    By.CLASS_NAME,
    value="_UuSG _3mBt0 _2z1u_ _30bXl _UuSG _3ejos ALevz".replace(" ", "."),
).get_attribute("src")

info["cover_photo"] = driver.find_element(
    By.CLASS_NAME,
    value="Os0yf _UuSG _3ejos ALevz".replace(" ", "."),
).get_attribute("src")

info["about"] = driver.find_element(
    By.CSS_SELECTOR,
    value="div._9utbn > p",
).text

# Elements with same class name for the number of gabs and followers/following
flw_elem = driver.find_elements(
    By.CLASS_NAME,
    value="_UuSG ALevz _3Ujf8 _1o5Ge _81_1w _1E64f _3ddB-".replace(" ", "."),
)
info["num_gabss"] = flw_elem[0].get_attribute("title")[:-5]
info["num_followers"] = flw_elem[1].get_attribute("title")[:-10]
info["num_following"] = flw_elem[2].get_attribute("title")[:-10]

# Elements containing the user's posts
post_elem = driver.find_elements(
    By.CSS_SELECTOR,
    value=f"a.{'_UuSG _3_54N L4pn5 _3Ujf8 _1o5Ge _81_1w _3TwRa _3OtSI ALevz'.replace(' ', '.')}",
)

post_ids = []
for elem in post_elem:
    post_ids.append(elem.get_attribute("href"))


# info["last_posts"]
# info["avg_engagement"]

for key, value in info.items():
    print(f"{key}: {value}")


# Close the browser
# driver.close()
driver.quit()
