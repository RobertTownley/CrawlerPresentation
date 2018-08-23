'''CRAWLER NUMBER TWO

This crawler takes control of my Google Chrome browser to visit webpages for us

It searches within Google Images for a term we care about, and then
saves all of those files into a folder.
'''
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from utils import save_image_from_internet


def wait():
    time.sleep(2)


def get_browser():
    options = webdriver.chrome.options.Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    browser = webdriver.Chrome(
        chrome_options=options,
        executable_path='/usr/local/bin/chromedriver',
    )
    return browser


# Start a selenium session
browser = get_browser()

# Visit a URL within Chrome
browser.get('https://google.com')

# Wait a few seconds (not for any reason, just so we can see it in action)
wait()

# Now go to Instagram
browser.get('https://instagram.com')

# Wait another few seconds
wait()

# Now go to Google Image Search
browser.get('https://images.google.com')

# Aaaand wait a second
wait()

# Find the Google search bar within our browser
google_search_bar = browser.find_element_by_id("lst-ib")

# "Type" in the word "puppies"
google_search_bar.send_keys("Puppies")

# Hit enter
google_search_bar.send_keys(Keys.ENTER)

# Wait again
wait()

# Grab a list of all images on the page, using CSS rules
images = browser.find_elements_by_css_selector("img.rg_ic.rg_i")

# With each image on the page...
for image in images:
    # ...check whether it's a hidden image...
    if image.is_displayed():
        # ... and if it is, click on it
        image.click()

        # ...then wait a bit for the image to load
        wait()

        active_image = browser.find_element_by_css_selector("img.irc_mi")
        url = active_image.get_attribute("src")
        save_image_from_internet(url)

# When we're done, close the Chrome window
browser.close()
