"""
Scraping a Single Gab User Profile by Benedict Castro | benedict.zcastro@gmail.com
"""

# Import needed modules
from bs4 import BeautifulSoup
import requests

# Declare global variables
URL = "https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock"


def main():
    """
    Scraping a Single Gab User Profile
    by Benedict Castro | benedict.zcastro@gmail.com
    :return: *******
    """

    # Request the content of the webpage
    response = requests.get(URL)

    # Parse through the response with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    print(soup)

    # # Extract the titles of the movies that are in a h3 tag and with a class name 'title'
    # title_tags = soup("h3", class_="title")
    # titles = [title.getText() for title in title_tags]

    # # Write the scraped movies to a text file
    # with open("movies.txt", "w", encoding="utf-8") as file:
    #     for _ in range(len(titles)):
    #         file.write(f"{titles[-(_+1)]}\n")


# If the program is run (instead of imported), run the program
if __name__ == "__main__":
    main()
