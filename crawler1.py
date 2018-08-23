'''CRAWLER NUMBER ONE

This crawler uses the Python "requests" library to grab data from NationalJournal.com.

It then loads the data it receives into a BeautifulSoup object to make it easier for us
to "parse" the HTML into Python.

Finally, we take the data that we care about from the returned data, and save it to
a CSV.
'''

import bs4
import requests

from utils import send_email

# Set the URL we want to see
url = "https://nationaljournal.com/dashboard"

# Use the Python "requests" library to get data from that URL
raw_data_from_scraper = requests.get(url)

# Grab the actual content from the raw data we receive back from "requests"
formatted_data_from_scraper = raw_data_from_scraper.content

# Pass the content into BeautifulSoup, a library for going through HTML data
website_content = bs4.BeautifulSoup(formatted_data_from_scraper, 'lxml')

# Find all HTML elements with an h3 tag, because that's how NJ displays headlines
headlines = website_content.find_all("h3")

# Go through each headline
for headline in set(headlines):

    # If that headline has the word "cats" in it...
    if "Republican" in headline.text:
        content = "NJ made a new article about Republicans: " + headline.text
        recipient = 'Me@RobertTownley.com'
        send_email(to=recipient, subject='NJ Update!!!', body=content)
