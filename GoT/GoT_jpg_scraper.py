# Import the libraries needed
import requests
import time
from bs4 import BeautifulSoup

# The URL to scrape
url = 'https://www.popsugar.com/celebrity/Kit-Harington-Rose-Leslie-Cutest-Pictures-42389549?stream_view=1#photo-42389576'
#url = 'https://www.bing.com/images/search?q=jon+snow&FORM=HDRSC2'

# Connecting
response = requests.get(url)

# Grab the HTML and using Beautiful
soup = BeautifulSoup (response.text, 'html.parser')

#A loop code to run through each link, and download it
for i in range(len(soup.findAll('img'))):

    tag = soup.findAll('img')[i]
    link = tag['src']

    #skip it if it doesn't start with http
    if "http" in full_link: 
        print("grabbed url: " + link)

        filename = str(i) + '.jpg'
        print("Download: " + filename)

        r = requests.get(link)
        open(filename, 'wb').write(r.content)

    else:
        print("grabbed url: " + link)
        print("skip")

    
    time.sleep(1)Breaking down the code