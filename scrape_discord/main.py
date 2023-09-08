#############################################################
# Discord Data Extraction using Selenium              #######
# by Benedict Z. Castro | benedict.zcastro@gmail.com  #######
#############################################################

# Import needed modules/libraries ###########################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Keep Chrome browser open after program finishes ###########
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create driver with Chrome #################################
driver = webdriver.Chrome(options=chrome_options)
# For maximizing window
driver.maximize_window()
# Gives an implicit wait for 20 seconds
driver.implicitly_wait(20)

# Main - Extract the information needed #####################


def main():
    # Create a list to store all user dictionary data
    servers_info = []
    # Create users list
    base_url = "https://discord.com/channels/"
    servers_list = ["916725085019181056"]

    # Define credentials
    ACCT_EMAIL = "YOUR EMAIL"
    ACCT_PASSWORD = "YOUR PASSWORD"

    for server in servers_list:
        # Request user data from website
        driver.get(base_url + server + "/customize-community")
        # The website takes time to load
        time.sleep(5)
        # Locate credentials fields for signing in
        email_field = driver.find_element(By.ID, value="uid_5")
        email_field.send_keys(ACCT_EMAIL)
        password_field = driver.find_element(By.NAME, value="password")
        password_field.send_keys(ACCT_PASSWORD)
        login_button = driver.find_element(
            By.CSS_SELECTOR,
            value=f'button.{"marginBottom8-emkd0_ button-1cRKG6 button-ejjZWC lookFilled-1H2Jvj colorBrand-2M3O3N sizeLarge-2xP3-w fullWidth-3M-YBR grow-2T4nbg".replace(" ", ".")}',
        )
        login_button.click()

        # Create a dictionary to contain all information
        info = {}

        info["server_name"] = driver.find_element(
            By.CSS_SELECTOR,
            value=f'div.{"lineClamp1-1voJi7 text-md-semibold-2VMhBr name-3Uvkvr".replace(" ", ".")}',
        ).text

        info["server_id"] = server

        info["members_count"] = (
            driver.find_element(
                By.CSS_SELECTOR,
                value="#channels > ul > li:nth-child(16)",
            )
            .get_attribute("data-dnd-name")
            .split()[1]
        )

        info["channels_count"] = driver.find_element(
            By.CSS_SELECTOR,
            value=f'div.{"textBadge-1fdDPJ base-3IDx3L eyebrow-132Xza baseShapeRound-3epLEv".replace(" ", ".")}',
        ).text

        # Navigate to a certain
        driver.get(base_url + server + "/1071466022395183164")

        last_message = driver.find_elements(
            By.CSS_SELECTOR, value="li.messageListItem-ZZ7v6g"
        )[-1]
        last_message_content = driver.find_element(
            By.CSS_SELECTOR, value="div.contents-2MsGLg"
        )
        info["last_message"] = {
            "user": last_message_content.find_element(
                By.CSS_SELECTOR, value="h3 > span:nth-child(1) > span"
            ).text,
            "text": last_message_content.find_element(
                By.CSS_SELECTOR, value="div"
            ).text,
            "media": last_message_content.find_element(
                By.CSS_SELECTOR, value="div img"
            ).get_attribute("src"),
            "time": last_message_content.find_element(
                By.CSS_SELECTOR, value="time"
            ).text,
        }

    servers_info.append(info)

    # Close the browser
    driver.quit()

    print(servers_info)

    # Save data to csv
    df = pd.DataFrame(servers_info)
    df.to_csv("discord_data.csv")


# Run the program
if __name__ == "__main__":
    main()
