import requests 
from bs4 import BeautifulSoup

r = requests.get("https://www.teamfortress.tv/user/Nintails")
print(r)

# We want to check the status code to ensure that we access the page

# Parsing the HTML
soup = BeautifulSoup(r.content, "html.parser")
# print(soup.prettify()) prints all HTML content

# We want to filter the full request for all links
s = soup.find('div', id="content")
postLinks = s.find_all("a")

# We want to store all links in an array.
print(postLinks)

# We want to open them and check for upfrags/downfrags.

# We want to summarize the findings.